from django.urls import include, path
from . import views

urlpatterns = [
  path('list/', views.list, name='list'),
  path('add/', views.add, name='add'),
]