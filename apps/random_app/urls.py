from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #this VIEWS the function INDEX in the views file
]
