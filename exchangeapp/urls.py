from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'exchange/', views.exchanger_form, name="exchanger_form"),
    url(r'history/', views.history, name="history")
]