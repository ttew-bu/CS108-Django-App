#urls.py
#Tristan Tew (ttew@bu.edu)
#Urls page for CSC database that will allow the 
#user to interact with pages within this application,
#complete delete/add methods, and navigate using hyperlinks

from django.urls import path, include #include allows us to use the built-in accounts feature
from .views import * #import the class definitions
from .models import * #import the model definitions 
from django.contrib import admin #added so that we can create a login for the app!

urlpatterns = [
    #this maps the URL to the view 
    path('', LandingPageView.as_view(), name="landingpage"),
    #will change to homepage

    path('home', HomePageView.as_view(), name='home'), 
    #landing page for after you sign in

    path('accounts', include('django.contrib.auth.urls')), 
    #allows us to run a login feature using admin

    path('partners', ShowAllCommunityPartnersView.as_view(), name='all_partners'), 
    #shows all partners

    path('volunteers', ShowAllVolunteersView.as_view(), name='all_volunteers'), 
    #shows all volunteers

    path('events', ShowAllEventsView.as_view(), name='all_events' ), 
    #shows all events

    path('partner/<int:pk>', ShowCommunityPartnerPageView.as_view(), name='show_partner'),
    #shows individual partners

    path('volunteer/<int:pk>', ShowVolunteerPageView.as_view(), name='show_volunteer'),
    #shows individual volunteers

    path('event/<int:pk>', ShowEventPageView.as_view(), name='show_event'),
    #shows individual events

    path('add_volunteer', CreateVolunteerView.as_view(), name='add_volunteer'),
    #creates volunteers

    path('add_partner', CreatePartnerView.as_view(), name='add_partner'),
    #creates partners

    path('add_event', CreateEventView.as_view(), name='add_event'),
    #creates event

    path('volunteer/<int:pk>/update', UpdateVolunteerView.as_view(), name='update_volunteer'),
    #takes current vol and updates it

    path('partner/<int:pk>/update', UpdatePartnerView.as_view(), name='update_partner'),
    #takes current partner and updates it

    path('event/<int:pk>/update', UpdateEventView.as_view(), name='update_event'),
    #takes current event and updates it

    path('volunteer/<int:pk>/assign', AssignVolView.as_view(), name='assign_vol'),
    #takes a volunteer and assigns them to an event

    path('event/<int:pk>/assign', AssignEventView.as_view(),name='assign_event'),
    #pulls up page to assign vols

    path('volunteer/<int:volunteer_pk>/add_to_event/<int:event_pk>', add_volunteer, name='add_to_event'),
    #allows us to add vols to events; doesn't use .as_view to use a function on the views page

    path('volunteer/<int:volunteer_pk>/add_vol_to_event/<int:event_pk>', add_volunteer_return_vol, name='add_vol_to_event'),
    #same as above, but redirects to a different url

    path('volunteer/<int:volunteer_pk>/remove_from_event/<int:event_pk>', remove_volunteer, name='remove_from_event'),
    #allows us to remove vols from events;doesn't use .as_view to use a function on the views page

    path('volunteer/<int:volunteer_pk>/remove_return_vol/<int:event_pk>', remove_volunteer_return_vol, name='remove_vol_from_event'),
    #same as function above, but with different redirect url
    
    path('partner/<int:partner_pk>/delete', DeletePartnerView.as_view(), name="delete_partner"), 
    #delete partner url

    path('volunteer/<int:volunteer_pk>/delete', DeleteVolunteerView.as_view(), name="delete_volunteer"), 
    #Delete volunteer url
    
    path('event/<int:event_pk>/delete', DeleteEventView.as_view(), name="delete_event"), 
    #delete event url

]