from django.contrib import messages
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from smartmin.views import SmartCRUDL, SmartCreateView, SmartListView
from .models import Transaction, Category


class CategoryCRUDL(SmartCRUDL):
    model = Category

    class Create(SmartCreateView):

        def get_success_url(self):
            animal_id = self.request.session.get('animal_id', None)
            return reverse('finances.transaction_create') + '?animal=' + animal_id


class TransactionCRUDL(SmartCRUDL):
    model = Transaction

    class FormMixin(object):
        def __init__(self, **kwargs):
            from .forms import TransactionForm
            self.form_class = TransactionForm
            super(TransactionCRUDL.FormMixin, self).__init__(**kwargs)

    class Create(FormMixin, SmartCreateView):
        fields = ('transaction_type', 'category', 'date', 'amount', )
        field_config = {
            'transaction_type': (dict(label='Type')),
            'category': dict(help=mark_safe('<a href="/finances/category/create/">Click here</a> to add new category')),
        }

        def get(self, request, *args, **kwargs):
            animal_id = request.GET.get('animal', None)
            group_id = request.GET.get('group', None)
            request.session['animal_id'] = animal_id
            if not animal_id and not group_id:
                messages.warning(request, 'Animal Id or group Id is required')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            return super(TransactionCRUDL.Create, self).get(request, *args, **kwargs)

        def get_success_url(self):
            return reverse('animals.animal_read', args=[self.request.GET.get('animal', None)])

    class List(SmartListView):
        fields = ('id', 'date', 'transaction_type', 'category', 'amount', )

        field_config = {
            'transaction_type': (dict(label='Type')),
        }

        def get_queryset(self, **kwargs):
            queryset = super(TransactionCRUDL.List, self).get_queryset(**kwargs)
            queryset = queryset.order_by('-id')
            return queryset
