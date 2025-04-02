from django.urls import path
from . import views

urlpatterns = [
    path('', views.donor_list, name='donor_list'),
    path('add/', views.add_donor, name='add_donor'),
    path('delete/<int:donor_id>/', views.delete_donor, name='delete_donor'),  # Delete URL
]
