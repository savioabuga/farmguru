from django import forms
from .models import Transaction, Category
from bootstrap3_datetime.widgets import DateTimePicker


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = ('name',)
        model = Category


class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), help_text='Add a new category', required=False)
    date = forms.DateField(widget=DateTimePicker(options={'format': 'YYYY-MM-DD', 'pickTime': False}), required=False)

    class Meta:
        model = Transaction
        exclude = ('group', 'animal')