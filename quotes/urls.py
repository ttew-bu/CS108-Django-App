#file: quotes/urls.py
#description: direct URL requests to view functions

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView # our class definition

urlpatterns = [
    #map the URL (empty string) to the view
    path('', RandomQuotePageView.as_view(), name="random"), #pick random quote
    path('all', HomePageView.as_view(), name='home'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), #show one quote
]