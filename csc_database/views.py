from django.shortcuts import render
from .models import *
from django.views.generic import *
from .forms import * 
from django.shortcuts import *
from django.urls import *

# Create your views here.

class ShowAllCommunityPartnersView(ListView):
    '''subclass of listview that displays all CPs'''
    model = CommunityPartner
    template_name= 'csc_database/all_partners.html'
    context_object_name = 'all_partners'

class ShowCommunityPartnerPageView(DetailView):
    '''subclass of detailview for info on one cp'''
    model = CommunityPartner
    template_name = 'csc_database/show_partner.html'
    context_object_name = 'partner'

class ShowAllVolunteersView(ListView):
    '''subclass of listview to display all volunteers'''
    model = Volunteer
    template_name = 'csc_database/all_volunteers.html'
    context_object_name = 'all_volunteers'

class ShowVolunteerPageView(DetailView):
    '''subclass of detailview to show an individual volunteer's information'''

    model = Volunteer
    template_name = 'csc_database/show_volunteer.html'
    context_object_name = 'volunteer'



