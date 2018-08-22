from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^login_page$', views.login_page, name='login_page'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^login$', views.login, name='login'),
    # url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^logout$', views.logout, name='logout')
]