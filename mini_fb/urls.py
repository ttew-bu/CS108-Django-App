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
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name='delete_status'), #delete a status URL
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name="news_feed"), #newsfeed url NEW!
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name="show_possible_friends"), #List of possible friends 
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name='add_friend'), #add friend button url
]