from django.urls import path
from . import views

urlpatterns = [
    path('ring_info/', views.ring_info, name='ring_info'),
    path('report/', views.report, name='report'),
]