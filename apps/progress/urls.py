from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show_record$', views.show_record, name='show_record'),
    url(r'^show_schedule$', views.show_schedule, name='show_schedule')
]