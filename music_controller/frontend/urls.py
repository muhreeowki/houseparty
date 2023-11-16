from django.urls import path
from ./views.py import index

urlpatterns = [
    path('', index)
]
