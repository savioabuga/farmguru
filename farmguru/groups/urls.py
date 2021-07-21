from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',

                       )


urlpatterns.extend(views.AnimalGroupCRUDL().as_urlpatterns())
urlpatterns.extend(views.TreatmentCRUDL().as_urlpatterns())
urlpatterns.extend(views.PastureCRUDL().as_urlpatterns())