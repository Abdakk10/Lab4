# taxapp/views.py

from django.shortcuts import render
from django.http import HttpResponse

def default_view(request):
    return render(request, 'taxapp/default.html')

def calculate_tax(request, any_number):
    try:
        # Try to convert the URL parameter to a float
        price = float(any_number)
        tax_rate = 0.15
        total_with_tax = price * (1 + tax_rate)
        return HttpResponse(f'Total with 15% tax: ${total_with_tax:.2f}')
    except ValueError:
        # Handle the case where the conversion fails
        return HttpResponse('Invalid input. Please provide a valid number.')

def tax_rate_view(request):
    tax_rate = 0.15
    return render(request, 'taxapp/tax_rate.html', {'tax_rate': tax_rate})
