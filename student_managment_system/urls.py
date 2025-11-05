from django.urls import path
from . import views

urlpatterns = [
  path('list/', views.list, name='list'),
  path('add/', views.add, name='add'),
  path('edit/<int:student_id>/', views.edit, name='edit'),
  path('delete/<int:student_id>/', views.delete, name='delete'),
]