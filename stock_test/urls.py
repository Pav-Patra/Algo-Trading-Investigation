from django.urls import path
from . import views

urlpatterns = [
    path('stock_test', views.stock_test, name='stock_test'),
]