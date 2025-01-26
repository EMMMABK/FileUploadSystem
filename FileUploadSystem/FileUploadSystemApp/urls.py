from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.show_data, name='show_data')
]