import string
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.template.context import RequestContext
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from smartmin.views import SmartCRUDL, SmartCreateView, SmartReadView, SmartUpdateView, SmartListView
from django_select2.views import Select2View, NO_ERR_RESP
from finances.views import TransactionCRUDL
from records.views import AnimalNoteCRUDL
from groups.models import AnimalGroup
from health.models import Treatment
from .models import Animal, Breed


class AnimalGroupSelect2View(Select2View):

    def get_results(self, request, term, page, context):
        # Fetch all by default
        groups = AnimalGroup.objects.all()

        # If there's actually a term, filter on it
        if term.strip() != '':
            groups = groups.filter(name__icontains=term)

        res = [(group.id, group.name) for group in groups]
        return (NO_ERR_RESP, False, res)  # Any error response, Has more results, options list


class AnimalsSelect2View(Select2View):

    def get_results(self, request, term, page, context):
        # Fetch all by default
        animals = Animal.objects.all()

        # If there's actually a term, filter on it
        if term.strip() != '':
            animals = animals.filter(name__icontains=term)

        res = [(animal.id, animal.name) for animal in animals]
        return (NO_ERR_RESP, False, res)  # Any error response, Has more results, options list


class TreatmentCRUDL(SmartCRUDL):
    model = Treatment

    class FormMixin(object):

        def __init__(self, **kwargs):
            # Prevent cyclic import errors
            from health.forms import TreatmentForm
            self.form_class = TreatmentForm
            super(TreatmentCRUDL.FormMixin, self).__init__(**kwargs)

    class Create(FormMixin, SmartCreateView):
        fields = ('date', 'description', 'notes')

        def get(self, request, *args, **kwargs):
            animal_id = request.GET.get('animal', None)
            if not animal_id:
                messages.warning(request, 'Animal Id is required')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            return super(TreatmentCRUDL.Create, self).get(request, *args, **kwargs)

        def post_save(self, obj):
            animal_id = self.request.GET.get('animal', None)
            try:
                animal = Animal.objects.get(id=animal_id)
            except Animal.DoesNotExist:
                messages.error(self.request, 'Animal Id is required')
            else:
                obj.animals.add(animal)
            return obj

        def get_success_url(self):
            return reverse('animals.animal_read', args=[self.request.GET.get('animal', None)])

    class Update(FormMixin, SmartUpdateView):
        fields = ('date', 'description', 'notes')

        def get_success_url(self):
            return reverse('animals.animal_read', args=[self.object.animal.id])

    class List(SmartListView):
        fields = ('id', 'type', 'date', 'description', 'notes')

        def get_queryset(self, **kwargs):
            queryset = super(TreatmentCRUDL.List, self).get_queryset(**kwargs)
            queryset = queryset.filter(animals=self.request.animal)
            return queryset


class AnimalCRUDL(SmartCRUDL):
    model = Animal

    class FormMixin(object):

        def __init__(self, **kwargs):
            # Prevent cyclic import errors
            from .forms import AnimalForm
            self.form_class = AnimalForm
            super(AnimalCRUDL.FormMixin, self).__init__(**kwargs)

        def customize_form_field(self, name, field):
            field = super(AnimalCRUDL.FormMixin, self).customize_form_field(name, field)
            try:
                animal = self.get_object()
                if name == 'group':
                    # Force the minimumInputLength to 0, so that it shows all the contacts by default
                    field.widget.options['minimumInputLength'] = 0
                    field.widget.choices = [(group.id, group.name) for group in animal.groups.order_by('name').all()]
                    field.initial = [group.id for group in animal.groups.order_by('name').all()]

            except AttributeError:
                pass

            return field

        def post_save(self, obj):
            """ Add groups """
            if 'group' in self.form.cleaned_data:
                for group in self.form.cleaned_data['group']:
                    try:
                        obj.groups.add(group)
                    except ValueError:
                        new_group, _ = AnimalGroup.objects.get_or_create(name=string.capwords(group))
                        if new_group and new_group not in obj.groups.all():
                            obj.groups.add(new_group)
            return obj

    class Create(FormMixin, SmartCreateView):
        pass

    class Read(SmartReadView):
        fields = ('animal_id', 'alt_id', 'electronic_id', 'ear_tag', 'name', 'color', 'gender', 'breed', 'sire', 'dam'
                  'status', 'birth_date', 'birth_weight', 'weaning_date', 'weaning_weight', 'yearling_date',
                  'yearling_weight')

        def get_context_data(self, **kwargs):
            context_data = super(AnimalCRUDL.Read, self).get_context_data(**kwargs)

            # Add related lists
            self.request.animal = self.object

            treatment_response = TreatmentCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(treatment_response, 'context_data'):
                treatment_response.context_data['add_url'] = reverse('animals.treatment_create') + '?animal=' + str(self.request.animal.id)
                context_data['treatment'] = render_to_string('health/treatment_related_list.html', treatment_response.context_data, RequestContext(self.request))

            note_response = AnimalNoteCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(note_response, 'context_data'):
                context_data['notes'] = render_to_string('records/animalnote_related_list.html', note_response.context_data, RequestContext(self.request))

            context_data['animal_documents'] = render_to_string('records/animaldocument.html', {'animal': self.request.animal}, RequestContext(self.request))

            transaction_response = TransactionCRUDL().view_for_action('list').as_view()(self.request)
            if hasattr(transaction_response, 'context_data'):
                transaction_response.context_data['add_url'] = reverse('finances.transaction_create') + '?animal=' + str(self.request.animal.id)
                context_data['transactions'] = render_to_string('finances/transaction_related_list.html', transaction_response.context_data, RequestContext(self.request))

            return context_data

    class Update(FormMixin, SmartUpdateView):
        pass

    class List(SmartListView):
        fields = ('id', 'name', 'color', 'breed', 'gender', 'sire', 'dam')


class BreedCRUDL(SmartCRUDL):
    model = Breed



