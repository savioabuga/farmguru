from django import forms
from django.core.urlresolvers import reverse
from django_select2.fields import HeavySelect2TagField, HeavySelect2MultipleChoiceField
from django_select2.widgets import HeavySelect2TagWidget, HeavySelect2MultipleWidget
from bootstrap3_datetime.widgets import DateTimePicker
from .models import Animal


class AnimalForm(forms.ModelForm):
    group = HeavySelect2TagField(label='Groups',
                                     required=False,
                                 help_text=u'Type to find existing groups or to create a new group.',
                                 widget=HeavySelect2TagWidget(data_url=reverse('animals_select_groups'), select2_options={'minimumInputLength': 0, 'placeholder': 'Select groups', 'width': '360px'}))

    birth_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)
    weaning_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)
    yearling_date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)

    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ('group',):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Animal
        fields = ('animal_id', 'alt_id', 'electronic_id', 'ear_tag', 'name', 'color', 'gender', 'breed', 'sire', 'dam',
                  'status', 'birth_date', 'birth_weight', 'weaning_date', 'weaning_weight', 'yearling_date',
                  'yearling_weight')

    def clean(self):
        cleaned_data = super(AnimalForm, self).clean()
        ear_tag = cleaned_data.get('ear_tag')
        name = cleaned_data.get('name')
        animal_id = cleaned_data.get('animal_id')
        electronic_id = cleaned_data.get('electronic_id')
        alt_id = cleaned_data.get('alt_id')
        if not ear_tag and not name and not animal_id and not electronic_id and not alt_id:
            raise forms.ValidationError('Some kind of identification is required')
        return cleaned_data
