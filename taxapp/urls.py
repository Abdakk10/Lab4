# taxapp/urls.py

from django.urls import path
from .views import default_view, calculate_tax, tax_rate_view

urlpatterns = [
    path('', default_view, name='default'),
    path('<str:any_number>/', calculate_tax, name='calculate_tax'),
    path('taxrate/', tax_rate_view, name='tax_rate'),
]
