from django.urls import path
from . import views

urlpatterns = [
    path('', views.combined_view, name='combined_view'),
]
