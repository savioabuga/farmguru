from django.db import models
from model_utils.models import TimeStampedModel


class Treatment(TimeStampedModel):
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    animals = models.ManyToManyField('animals.Animal', null=False, blank=False, related_name='treatment')
    animalgroup = models.ForeignKey('groups.AnimalGroup', null=True, blank=False)