#file: quotes/urls.py
#description: direct URL requests to view functions

from django.urls import path
from .views import * # HomePageView, QuotePageView, PersonPageView, RandomQuotePageView # our class definition

urlpatterns = [
    #map the URL (empty string) to the view
    path('', RandomQuotePageView.as_view(), name="random"), #pick random quote
    path('all', HomePageView.as_view(), name='all'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), #show one quote
    path('quote/<int:pk>/update', UpdateQuoteView.as_view(), name='update_quote'), #update
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), #show one person
    path('create_quote', CreateQuoteView.as_view(), name='create_quote'), #create new quote
]