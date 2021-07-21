from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel
from model_utils import Choices


class Breed(TimeStampedModel):
    name = models.CharField(max_length=30)
    gestation_period = models.IntegerField(max_length=4)


class Animal(TimeStampedModel):
    # Choices
    STATUS_CHOICES = Choices(('active', _('Active')), )
    COLOR_CHOICES = Choices(('yellow', _('Yellow')), )
    GENDER_CHOICES = Choices(('bull', _('Bull')), ('cow', _('Cow')))

    # Identification
    animal_id = models.CharField(max_length=30, blank=True)
    alt_id = models.CharField(max_length=30, blank=True)
    electronic_id = models.CharField(max_length=30, blank=True)
    ear_tag = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=30, blank=True)

    # Description
    color = models.CharField(choices=COLOR_CHOICES, max_length=20, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    breed = models.ForeignKey(Breed, null=True, blank=True)
    sire = models.ForeignKey('self', null=True, blank=True, related_name='animal_sire')
    dam = models.ForeignKey('self', null=True, blank=True, related_name='animal_dam')

    # Status
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES.active, max_length=20, blank=True)

    # Calfhood
    birth_date = models.DateField(null=True, blank=True)
    birth_weight = models.IntegerField(max_length=4, null=True, blank=True)
    weaning_date = models.DateField(null=True, blank=True)
    weaning_weight = models.IntegerField(max_length=4, null=True, blank=True)
    yearling_date = models.DateField(null=True, blank=True)
    yearling_weight = models.IntegerField(max_length=4, null=True, blank=True)

    def __unicode__(self):
        return self.ear_tag

