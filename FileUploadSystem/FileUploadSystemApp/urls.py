from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.show_data, name='show_data'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
]