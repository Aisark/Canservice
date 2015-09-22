from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^Canservice/$',views.inicio),
    url('Canservice/Registro$',views.registro,name='registro'),
]