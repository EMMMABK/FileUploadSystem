from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.show_data, name='show_data'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]