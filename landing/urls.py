from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('s/', s, name='s'),
]
