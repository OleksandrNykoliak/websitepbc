from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage_view, name='homepage'),
    # path('projects/', projects_view, name='projects'),
    # path('about/', about_view, name='about'),
    # path('about2/', about2_view, name='about2'),
    # path('services/', services_view, name='services'),
    # path('team/', team_view, name='team'),
    # path('customers/', customer_view, name='customers'),
    # path('contact/', contact_view, name='contact'),
]
