from django.shortcuts import render

# Create your views here.

from .models import Quote
from django.views.generic import ListView

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes'''

    model = Quote #retrieve objects of type Quote from the db
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list' #how to find the template file