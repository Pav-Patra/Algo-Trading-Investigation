from django.urls import path 
from . import views

urlpatterns = [
    path('', views.get_stock),
    path('test/', views.simple_view, name='test'),
    path('asset/<str:asset_name>/', views.asset_graph_view, name='asset_graph'),
]