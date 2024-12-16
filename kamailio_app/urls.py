from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.filter_and_crud, name='filter_and_crud'),
]
