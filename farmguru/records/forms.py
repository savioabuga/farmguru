from django import forms
from django.conf import settings
from bootstrap3_datetime.widgets import DateTimePicker
from .models import AnimalNote, AnimalGroupNote


class NoteForm(forms.Form):
    date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)
    file = forms.FileField()
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}))

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Media:
        css = {
            'screen': (settings.STATIC_URL + 'js/plugins/jasnyBootstrap/jasny-bootstrap.min.css',)
        }
        js = (settings.STATIC_URL + 'js/plugins/jasnyBootstrap/jasny-bootstrap.min.js',)


class AnimalNoteForm(NoteForm, forms.ModelForm):
    class Meta:
        model = AnimalNote
        fields = ('date', 'details', 'file')


class AnimalGroupNoteForm(NoteForm, forms.ModelForm):
    class Meta:
        model = AnimalGroupNote
        fields = ('date', 'details', 'file')
