from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^offer_help$', views.offer_help, name='offer_help'),
    url(r'^request_help$', views.request_help, name='request_help'),
]