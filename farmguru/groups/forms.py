from django import forms
from django.core.urlresolvers import reverse
from django_select2.fields import HeavySelect2MultipleChoiceField
from django_select2.widgets import HeavySelect2MultipleWidget
from .models import AnimalGroup, Pasture


class AnimalGroupForm(forms.ModelForm):
    members = HeavySelect2MultipleChoiceField(label='Members',
                                              required=False,
                                              help_text=u'Type to find animals',
                                              widget=HeavySelect2MultipleWidget(data_url=reverse('animals_select_animals'), select2_options={'minimumInputLength': 0, 'placeholder': 'Select Members', 'width': 'resolve'}))

    def __init__(self, *args, **kwargs):
        super(AnimalGroupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ('members',):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = AnimalGroup


class PastureForm(forms.ModelForm):
    members = HeavySelect2MultipleChoiceField(label='Members',
                                              required=False,
                                              help_text=u'Type to find animals',
                                              widget=HeavySelect2MultipleWidget(data_url=reverse('animals_select_animals'), select2_options={'minimumInputLength': 0, 'placeholder': 'Select Members', 'width': 'resolve'}))

    def __init__(self, *args, **kwargs):
        super(PastureForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ('members',):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pasture
        fields = ('name', 'acreage', 'members')