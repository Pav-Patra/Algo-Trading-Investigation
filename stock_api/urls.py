from django.urls import path 
from . import views

urlpatterns = [
    path('', views.get_stock),
    path('/test', views.simple_view)
]