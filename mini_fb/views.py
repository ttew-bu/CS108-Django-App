from django.shortcuts import render

#file:views.py
#author: Tristan Tew (ttew@bu.edu)
#description: views file for mini facebook

# Create your views here.

from .models import Profile
from django.views.generic import ListView, DetailView

class ShowAllProfilesView(ListView):
    ''' subclass of listview to display all profiles'''
    model = Profile #pulls objects for the Profile type from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'show_all_profiles'

class ShowProfilePageView(DetailView): #new view to show indiviudal profiles
    '''subclass of detailview for an individual profile'''
    model = Profile #using profile data
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'