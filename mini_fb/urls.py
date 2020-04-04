#file: urls.py
#author: tristan tew (ttew@bu.edu)
#description: the urls page for the mini_fb case 

from django.urls import path
from .views import * #import the mini fb class definitions import 
from .models import *

urlpatterns = [
    #this maps the URL to the view 
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), #new url; deleted and added back from GitHub
    path('create_profile',CreateProfileView.as_view(), name='create_profile'), #create profile url
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'), #update profile url
    path('profile/<int:pk>/post_status', create_status_message, name='post_status'), #post status message url
]