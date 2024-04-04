from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='hompage'),
    path('second/', views.my_view, name='secondpage'),  # Added comma after 'second/'
]
