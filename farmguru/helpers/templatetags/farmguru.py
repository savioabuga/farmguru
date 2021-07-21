from django import template
from django_select2.fields import HeavySelect2MultipleChoiceField

register = template.Library()


@register.filter
def select2(value):
    if type(value.field) is HeavySelect2MultipleChoiceField:
        return True
    return False