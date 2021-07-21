from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.template.context import RequestContext
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from smartmin.views import SmartCRUDL, SmartCreateView, SmartReadView, SmartListView, SmartUpdateView
from records.views import AnimalGroupNoteCRUDL
from finances.views import TransactionCRUDL
from health.views import TreatmentCRUDL
from health.models import Treatment
from .models import AnimalGroup, Pasture


class TreatmentCRUDL(SmartCRUDL):
    model = Treatment

    class FormMixin(object):

        def __init__(self, **kwargs):
            self.fields = ('date', 'animals', 'description', 'notes')
            # Prevent cyclic import errors
            from health.forms import TreatmentForm
            self.form_class = TreatmentForm
            super(TreatmentCRUDL.FormMixin, self).__init__(**kwargs)

        def customize_form_field(self, name, field):
            field = super(TreatmentCRUDL.FormMixin, self).customize_form_field(name, field)

            if name == 'animals':
                # Force the minimumInputLength to 0, so that it shows all the contacts by default
                field.widget.options['minimumInputLength'] = 0

                try:
                    treatment = self.get_object()
                    animalgroup = treatment.animalgroup
                    field.widget.choices = [(member.id, member.name) for member in animalgroup.members.order_by('name').all()]
                    field.initial = [member.id for member in treatment.animals.order_by('name').all()]

                except AttributeError:
                    group_id = self.request.GET.get('group', None)
                    animalgroup = AnimalGroup.objects.get(id=group_id)
                    field.widget.choices = [(member.id, member.name) for member in animalgroup.members.order_by('name').all()]
                    field.initial = [member.id for member in animalgroup.members.order_by('name').all()]

            return field

    class Create(FormMixin, SmartCreateView):

        def get(self, request, *args, **kwargs):
            group_id = request.GET.get('group', None)
            if not group_id:
                messages.warning(request, 'Group Id is required')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            return super(TreatmentCRUDL.Create, self).get(request, *args, **kwargs)

        def pre_save(self, obj):
            group_id = self.request.GET.get('group', None)
            try:
                animalgroup = AnimalGroup.objects.get(id=group_id)
            except AnimalGroup.DoesNotExist:
                messages.error(self.request, 'Grooup Id is required')
            else:
                obj.animalgroup = animalgroup
            return obj

        def get_success_url(self):
            return reverse('groups.animalgroup_read', args=[self.request.GET.get('group', None)])

    class Update(FormMixin, SmartUpdateView):

        def get_success_url(self):
            return reverse('groups.animalgroups_read', args=[self.object.animal.id])

    class List(SmartListView):
        fields = ('id', 'type', 'date', 'description', 'notes')

        def get_queryset(self, **kwargs):
            queryset = super(TreatmentCRUDL.List, self).get_queryset(**kwargs)
            queryset = queryset.filter(animalgroup=self.request.animalgroup)
            return queryset


class AnimalGroupCRUDL(SmartCRUDL):
    model = AnimalGroup

    class FormMixin(object):
        def __init__(self, **kwargs):
            # Prevent cyclic import errors
            from .forms import AnimalGroupForm
            self.form_class = AnimalGroupForm
            super(AnimalGroupCRUDL.FormMixin, self).__init__(**kwargs)

        def customize_form_field(self, name, field):
            field = super(AnimalGroupCRUDL.FormMixin, self).customize_form_field(name, field)
            try:
                animalgroup = self.get_object()
                if name == 'members':

                    # Force the minimumInputLength to 0, so that it shows all the contacts by default
                    field.widget.options['minimumInputLength'] = 0
                    field.widget.choices = [(member.id, member.name) for member in animalgroup.members.order_by('name').all()]
                    field.initial = [member.id for member in animalgroup.members.order_by('name').all()]

            except AttributeError:
                pass

            return field

    class Create(FormMixin, SmartCreateView):
        fields = ('name', 'members',)

    class Read(SmartReadView):
        fields = ('name', 'members', 'created', 'modified')

        def get_members(self, obj):
            members = ''
            for member in obj.members.all():
                members += '<a href=' + reverse('animals.animal_read', args=[member.id]) + '>' + str(member) + '</a>, '
            return members[:-2]

        def get_context_data(self, **kwargs):
            context_data = super(AnimalGroupCRUDL.Read, self).get_context_data(**kwargs)

            self.request.animalgroup = self.object

            animalgroupnote_response = AnimalGroupNoteCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(animalgroupnote_response, 'context_data'):
                context_data['animalgroupnotes'] = render_to_string('records/animalgroupnote_related_list.html', animalgroupnote_response.context_data, RequestContext(self.request))

            treatment_response = TreatmentCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(treatment_response, 'context_data'):
                treatment_response.context_data['add_url'] = reverse('groups.treatment_create') + '?group=' + str(self.request.animalgroup.id)
                context_data['treatment'] = render_to_string('health/treatment_related_list.html', treatment_response.context_data, RequestContext(self.request))

            transaction_response = TransactionCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(transaction_response, 'context_data'):
                transaction_response.context_data['add_url'] = reverse('finances.transaction_create') + '?group=' + str(self.request.animalgroup.id)
                context_data['transactions'] = render_to_string('finances/transaction_related_list.html', transaction_response.context_data, RequestContext(self.request))

            return context_data

    class Update(FormMixin, SmartUpdateView):
        fields = ('name', 'members',)

    class List(SmartListView):
        fields = ('id', 'name', 'members')

        def get_members(self, obj):
            members = ''
            for member in obj.members.all():
                members += '<a href=' + reverse('animals.animal_read', args=[member.id]) + '>' + str(member) + '</a>, '
            return members[:-2]


class PastureCRUDL(SmartCRUDL):
    model = Pasture

    class FormMixin(object):
        def __init__(self, **kwargs):
            # Prevent cyclic import errors
            from .forms import PastureForm
            self.form_class = PastureForm
            super(PastureCRUDL.FormMixin, self).__init__(**kwargs)

        def customize_form_field(self, name, field):
            field = super(PastureCRUDL.FormMixin, self).customize_form_field(name, field)
            try:
                pasture = self.get_object()
                if name == 'members':
                    # Force the minimumInputLength to 0, so that it shows all the contacts by default
                    field.widget.options['minimumInputLength'] = 0
                    field.widget.choices = [(member.id, member.name) for member in pasture.members.order_by('name').all()]
                    field.initial = [member.id for member in pasture.members.order_by('name').all()]

            except AttributeError:
                pass

            return field

    class Create(FormMixin, SmartCreateView):
        fields = ('name', 'acreage', 'members',)

    class Read(SmartReadView):
        fields = ('id', 'name', 'acreage', 'members', 'created', 'modified')

        def get_members(self, obj):
            members = ''
            for member in obj.members.all():
                members += '<a href=' + reverse('animals.animal_read', args=[member.id]) + '>' + str(member) + '</a>, '
            return members[:-2]

    class Update(FormMixin, SmartUpdateView):
        fields = ('name', 'acreage', 'members',)

    class List(SmartListView):
        fields = ('id', 'name', 'acreage', 'members')

        def get_members(self, obj):
            members = ''
            for member in obj.members.all():
                members += '<a href=' + reverse('animals.animal_read', args=[member.id]) + '>' + str(member) + '</a>, '
            return members[:-2]
