#urls.py
#Tristan Tew (ttew@bu.edu)
#Urls page for CSC database that will allow the 
#user to interact with pages within this application

from django.urls import path
from .views import * #import the class definitions
from .models import * #import the model definitions 

urlpatterns = [
    #this maps the URL to the view 
    path('', ShowAllCommunityPartnersView.as_view(), name='home'),#will change to homepage
    path('partners', ShowAllCommunityPartnersView.as_view(), name='all_partners'),
    path('volunteers', ShowAllVolunteersView.as_view(), name='all_volunteers'),
    path('partner/<int:pk>', ShowCommunityPartnerPageView.as_view(), name='show_partner'),
    path('volunteer/<int:pk>', ShowVolunteerPageView.as_view(), name='show_volunteer')

]