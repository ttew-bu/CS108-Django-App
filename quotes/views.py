from django.shortcuts import render

# Create your views here.

from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import *
from .forms import *
import random
from django.urls import *
from django.shortcuts import *

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes'''

    model = Quote #retrieve objects of type Quote from the db
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list' #how to find the template file

class QuotePageView(DetailView):
    '''Show the details for one quote'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    '''Show a random quote's details'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    # pick one at random
    def get_object(self):
        '''return a single instance of the Quote object, randomly selected'''

        #get all quotes
        all_quotes = Quote.objects.all()

        #pick one at random
        r = random.randint(0, (len(all_quotes)-1))
        q = all_quotes[r]
        return q #return this object
class PersonPageView(DetailView):
    '''Show all quotes and all images for one person'''

    model = Person
    template_name = 'quotes/person.html'
    #context_object_name = 'person'

    def get_context_data(self, **kwargs):
        '''returns a dictionary with context data for this template to use.'''

        #get default context data
        #this will include the person record
        context = super(PersonPageView, self).get_context_data(**kwargs)

        #create add image form:
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        # return the context dictionary:
        return context
class CreateQuoteView(CreateView):
    '''A view to create a new quote and save it to the db'''

    form_class = CreateQuoteForm
    template_name = "quotes/create_quote.html"

class UpdateQuoteView(UpdateView):
    '''A view to create a new quote and save it to the db'''

    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote.html"
    queryset = Quote.objects.all()

class DeleteQuoteView(DeleteView):
    '''A view to deletea  quote and remove it to the db'''

    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()
    success_url = "../../all" # what to do after deletion

    def get_success_url(self):
        '''Return the URL to which we are redirected upon deletion'''

        # get the pk for the quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first() #get one object from QUeryset
        # find the person associated with the quote

        # reverse to show the person page
        person = quote.person

        return reverse('person', kwargs={'pk':person.pk})
    
def add_image(request, pk):
    '''A custom view function to handle the submission of an image upload'''

    # find the  person for whom we are submitting the image
    person = Person.objects.get(pk=pk)
    # read request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)

    #check if the form is valid, save if so
    if form.is_valid():

            image = form.save(commit=False) #create the Image object, but not save
            image.person = person
            image.save() #store in db
    else:
        print("Error: the form was not valid")
    # redirect to a new URL, display person page
    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)
