# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
   # URL pattern for the AnimalGroupSelect2View
   url(regex=r'^animals-select-groups/$',
       view=views.AnimalGroupSelect2View.as_view(),
       name='animals_select_groups'
       ),
    # URL pattern for the AnimalsSelect2View
    url(
        regex=r'^animals-select-animals/$',
        view=views.AnimalsSelect2View.as_view(),
        name='animals_select_animals'
    ),
)

urlpatterns.extend(views.AnimalCRUDL().as_urlpatterns())
urlpatterns.extend(views.BreedCRUDL().as_urlpatterns())
urlpatterns.extend(views.TreatmentCRUDL().as_urlpatterns())

