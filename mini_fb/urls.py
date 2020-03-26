#file: urls.py
#author: tristan tew (ttew@bu.edu)
#description: the urls page for the mini_fb case 

from django.urls import path
from .views import ShowAllProfilesView #import the mini fb class definition

urlpatterns = [
    #this maps the URL to the view 
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles')
]