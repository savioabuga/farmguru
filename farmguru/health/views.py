from smartmin.views import SmartCRUDL, SmartCreateView, SmartUpdateView, SmartListView
from groups.models import AnimalGroup
from .models import Treatment


class TreatmentCRUDL(SmartCRUDL):
    model = Treatment

    class FormMixin(object):

        def __init__(self, **kwargs):
            # Prevent cyclic import errors
            from .forms import TreatmentForm
            self.form_class = TreatmentForm
            super(TreatmentCRUDL.FormMixin, self).__init__(**kwargs)

    class Create(FormMixin, SmartCreateView):
        fields = ('date', 'description', 'animals', 'notes')

    class Update(FormMixin, SmartUpdateView):
        pass

    class List(SmartListView):
        fields = ('id', 'animalgroup', 'date', 'description', 'notes')
        field_config = {
            'animalgroup': dict(label='Group'),
        }

        def get_queryset(self, **kwargs):
            queryset = super(TreatmentCRUDL.List, self).get_queryset(**kwargs)
            return queryset