from django.db import models
from model_utils.models import TimeStampedModel


class AnimalGroup(TimeStampedModel):
    name = models.CharField(max_length=30, blank=True)
    members = models.ManyToManyField('animals.animal', related_name='groups', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Pasture(TimeStampedModel):
    name = models.CharField(max_length=30, blank=True)
    acreage = models.IntegerField(max_length=10, null=True, blank=True)
    members = models.ManyToManyField('animals.Animal', related_name='pastures', null=True, blank=True)

    def __unicode__(self):
        return self.name