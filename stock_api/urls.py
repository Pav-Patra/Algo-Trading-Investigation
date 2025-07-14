from django.urls import path 
from . import views

urlpatterns = [
    path('', views.get_stock),
    path('test/', views.simple_view, name='test'),
    path('landingpage/', views.landing_page_view, name='landing_page_view'),
    path('asset/<str:asset_name>/', views.asset_graph_view, name='asset_graph'),
    path('assets/', views.get_all_assets)
]