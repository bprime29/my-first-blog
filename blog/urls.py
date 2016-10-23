from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.home, name='home'),

    url(r'^register/$', views.register, name='register'),
]