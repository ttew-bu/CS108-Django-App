from django.shortcuts import render

#file:views.py
#author: Tristan Tew (ttew@bu.edu)
#description: views file for mini facebook; includes two functions directly given in assignment 17 for 
# get context data and for create status message

# Create your views here.

from .models import *
from django.views.generic import *
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllProfilesView(ListView):
    ''' subclass of listview to display all profiles'''
    model = Profile #pulls objects for the Profile type from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'show_all_profiles'

class ShowProfilePageView(DetailView): #new view to show indiviudal profiles; deleted somehow and retrieved from GitHub
    '''subclass of detailview for an individual profile'''
    model = Profile #using profile data
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'

    #allows us to use the create_status_form URL and interact with the template
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

    # obtain the default context data (a dictionary) from the superclass; 
    # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
    # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
    # return this context dictionary
        return context

class CreateProfileView(CreateView):
    ''' subclass of createview to display new profile'''
    form_class = CreateProfileForm #form can be found on the .forms file
    template_name = "mini_fb/create_profile_form.html" #the location of the template within the django directory

class UpdateProfileView(UpdateView):
    '''A view to update a profile'''

    form_class = UpdateProfileForm #form can be found on the .forms file
    template_name = "mini_fb/update_profile_form.html" #the location of the template within the django directory
    queryset = Profile.objects.all() #allows all objects of the Profile to be accessed

def create_status_message(request, pk):
    '''Process a form submission to post a new status message.'''
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']

        # save the new status message object to the database
        if message:

            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            sm.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))