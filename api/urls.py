from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_list), 
    path('create/', views.create_student),
    path('delete/<int:pk>/', views.delete_student),
    path('update/<int:pk>/', views.update_student),
]
