from django.shortcuts import render

#file:views.py
#author: Tristan Tew (ttew@bu.edu)
#description:

# Create your views here.

from .models import Profile
from django.views.generic import ListView

class ShowAllProfilesView(ListView):
    ''' subclass of listview to display all profiles'''
    model = Profile #pulls objects for the Profile type from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'show_all_profiles'

