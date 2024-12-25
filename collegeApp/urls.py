from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('academics/', views.academics, name='academics'),
    path('academics/<str:branch_name>/', views.branch_detail, name='branch_detail'),
]
