from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel
from model_utils import Choices


class Category(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Transaction(TimeStampedModel):

    types = Choices(('income', _('Income')), ('expense', _('Expense')))

    category = models.ForeignKey(Category, blank=True, null=True)
    date = models.DateField()
    amount = models.IntegerField()
    animal = models.ForeignKey('animals.Animal', blank=True, null=True)
    animalgroup = models.ForeignKey('groups.AnimalGroup', blank=True, null=True)
    transaction_type = models.CharField(max_length=20, choices=types, default=types.income)
