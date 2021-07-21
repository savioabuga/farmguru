from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',)
urlpatterns.extend(views.TransactionCRUDL().as_urlpatterns())
urlpatterns.extend(views.CategoryCRUDL().as_urlpatterns())