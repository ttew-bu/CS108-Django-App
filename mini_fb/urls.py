#file: urls.py
#author: tristan tew (ttew@bu.edu)
#description: the urls page for the mini_fb case 

from django.urls import path
from .views import * #import the mini fb class definitions import 

urlpatterns = [
    #this maps the URL to the view 
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page') #new url
]