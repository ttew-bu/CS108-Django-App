from django.shortcuts import render

#file:views.py
#author: Tristan Tew (ttew@bu.edu)
#description: views file for mini facebook; includes two functions directly given in assignment 17 for 
# get context data and for create status message

# Create your views here.

from .models import *
from django.views.generic import *
from .forms import *
from django.shortcuts import *
from django.urls import *

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

class DeleteStatusMessageView(DeleteView):
    '''View to delete a status message'''
    
    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()
    #success_url = "../../show_all_profiles" this success url was used for testing purposes, 
    # but we now have a function for this to run correctly and display an individual profile 

    def get_context_data(self,**kwargs):
        '''returns a dictionary with context data for the template'''

        #get the context data for the exact message that we are trying to delete
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        #define the status that we are looking for with a primary key lookup 
        # and put it in the context dictionary 
        status = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        
        context['status']=status # adds this to the dictionary 
        
        #return the context dictionary:
        return context
    
    def get_object(self):
        '''returns the status message to be deleted'''
        
        # read the URL data values into variables, this is given in the assignment page
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        status = StatusMessage.objects.get(pk=status_pk)

        #return the status that we want    
        return status

    def get_success_url(self):
        '''Return the URL to which we are redirected upon deletion'''

        # read the URL data values into variables, both pk definitions were given in the assignment page
        profile_pk = self.kwargs['profile_pk'] #gives us the pk of the profile; 
        
        #we can use this for the reverse function instead of looking it up filtering through statuses
        status_pk = self.kwargs['status_pk'] #pk for status

        #find the status itself
        status = StatusMessage.objects.filter(pk=status_pk).first()


        #reverse and show the profile page
        page = reverse('show_profile_page', kwargs={'pk':profile_pk})
        return page

def create_status_message(request, pk):
    '''Process a form submission to post a new status message.'''

    # find the profile that matches the "pk" in the URL
    profile = Profile.objects.get(pk=pk)

    #name the form you want to process the request with 
    form = CreateStatusMessageForm(request.POST or None, request.FILES or None) #without the files request, it wont' add pictures. 

    # The method below is from a previous assignment. If not commented out, it will create a double post when creating a status. 
    # if and only if we are processing a POST request, try to read the data; OLD for assignment 17
    # if request.method == 'POST':

    #     # read the data from this form submission
    #     message = request.POST['message']

    #     # save the new status message object to the database
    #     if message:

    #         sm = StatusMessage()
    #         sm.profile = profile
    #         sm.message = message
    #         sm.save()

    # NEW for assignment 18 creates statuses with images by checking that we're using a valid form; makes form 17 redundant

    if form.is_valid: 
        status = form.save(commit=False) # create the status object, but don't save it
        status.profile = profile # map the status to the profile
        status.save() #save the status to the profile

    # redirect to the profile, pre-submission

    url = reverse('show_profile_page', kwargs={'pk':pk})
    return redirect(url)