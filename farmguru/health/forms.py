from django import forms
from django.core.urlresolvers import reverse
from bootstrap3_datetime.widgets import DateTimePicker
from django_select2.fields import HeavySelect2MultipleChoiceField
from django_select2.widgets import HeavySelect2MultipleWidget
from .models import Treatment


class TreatmentForm(forms.ModelForm):
    date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}), required=False)
    animals = HeavySelect2MultipleChoiceField(required=True,
                                              widget=HeavySelect2MultipleWidget(data_url=reverse('animals_select_animals'), select2_options={'minimumInputLength': 0, 'placeholder': 'Select Animals', 'width': 'resolve'}))

    def __init__(self, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ('animals', 'notes'):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Treatment
