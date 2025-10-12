from django.urls import path 
from . import views

urlpatterns = [
    path('landingpage/', views.landing_page_view, name='landing_page_view'),
    path('asset/<str:asset_name>/', views.asset_graph_view, name='asset_graph'),
    path('assets/', views.get_all_assets),
    path('asset/percentchange/<str:asset_name>/<int:minutes>/', views.get_percentage_change, name='asset_percent_change'),
    path('asset/percentchange/<int:minutes>/', views.get_all_percent_change, name='all_asset_percent_change')
]