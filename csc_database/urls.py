#urls.py
#Tristan Tew (ttew@bu.edu)
#Urls page for CSC database that will allow the 
#user to interact with pages within this application

from django.urls import path, include
from .views import * #import the class definitions
from .models import * #import the model definitions 
from django.contrib import admin #added so that we can create a login for the app!

urlpatterns = [
    #this maps the URL to the view 
    path('', LandingPageView.as_view(), name="landingpage"),#will change to homepage
    path('home', HomePageView.as_view(), name='home'), #landing page for after
    path('/accounts', include('django.contrib.auth.urls')), #allows us to run a login feature using admin
    path('partners', ShowAllCommunityPartnersView.as_view(), name='all_partners'),
    path('volunteers', ShowAllVolunteersView.as_view(), name='all_volunteers'),
    path('events', ShowAllEventsView.as_view(), name='all_events' ),
    path('partner/<int:pk>', ShowCommunityPartnerPageView.as_view(), name='show_partner'),
    path('volunteer/<int:pk>', ShowVolunteerPageView.as_view(), name='show_volunteer'),
    path('event/<int:pk>', ShowEventPageView.as_view(), name='show_event'),
    path('add_volunteer', CreateVolunteerView.as_view(), name='add_volunteer'),
    path('add_partner', CreatePartnerView.as_view(), name='add_partner'),
    path('add_event', CreateEventView.as_view(), name='add_event'),
    path('volunteer/<int:pk>/update', UpdateVolunteerView.as_view(), name='update_volunteer'),
    path('partner/<int:pk>/update', UpdatePartnerView.as_view(), name='update_partner'),
    path('event/<int:pk>/update', UpdateEventView.as_view(), name='update_event'),
    path('volunteer/<int:pk>/assign', AssignVolView.as_view(), name='assign_vol'),
    path('event/<int:pk>/assign', AssignEventView.as_view(),name='assign_event'),
    path('volunteer/<int:volunteer_pk>/add_to_event/<int:event_pk>', add_volunteer, name='add_to_event'),
    path('volunteer/<int:volunteer_pk>/remove_from_event/<int:event_pk>', remove_volunteer, name='remove_from_event'),
    path('partner/<int:partner_pk>/delete', DeletePartnerView.as_view(), name="delete_partner"), 
    path('volunteer/<int:volunteer_pk>/delete', DeleteVolunteerView.as_view(), name="delete_volunteer"), 
    path('event/<int:event_pk>/delete', DeleteEventView.as_view(), name="delete_event"), 

]