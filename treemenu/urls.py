from django.urls import path
from .views import my_view

urlpatterns = [
    path('view/', my_view, name='my-view'),
]
