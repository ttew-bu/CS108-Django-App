#name:views.py
#author: tristan tew (ttew@bu.edu)
#description: This file houses the class used to display database
#information, create/delete/update them, and to add the ability to
#add or subtract volunteers from individual events

from django.shortcuts import render
from .models import *
from django.views.generic import *
from .forms import * 
from django.shortcuts import *
from django.urls import *
from django.utils import *

# Create your views here.

class ShowAllCommunityPartnersView(ListView):
    '''subclass of listview that displays all CPs'''

    model = CommunityPartner

    template_name= 'project/all_partners.html'

    context_object_name = 'all_partners'

    #I put a queryset on the listview to order it
    queryset = CommunityPartner.objects.all().order_by('cp_name')

class ShowCommunityPartnerPageView(DetailView):
    '''subclass of detailview for info on one cp'''

    model = CommunityPartner

    template_name = 'project/show_partner.html'

    context_object_name = 'partner'

class ShowAllVolunteersView(ListView):
    '''subclass of listview to display all volunteers'''

    model = Volunteer

    template_name = 'project/all_volunteers.html'

    context_object_name = 'all_volunteers'

    #Queryset is on the listview to order it on the pages
    queryset=Volunteer.objects.all().order_by('bu_id')

class ShowVolunteerPageView(DetailView):
    '''subclass of detailview to show an individual volunteer's information'''

    model = Volunteer

    template_name = 'project/show_volunteer.html'

    context_object_name = 'volunteer'

class ShowAllEventsView(ListView):
    '''subclass of listview to display all Events'''

    model = ServiceEvent

    template_name = 'project/all_events.html'

    context_object_name = 'all_events'

    #Queryset is on the listview to order it chronologically
    queryset = ServiceEvent.objects.all().order_by('service_date')

class ShowEventPageView(DetailView):
    '''subclass of detailview to show an individual volunteer's information'''

    model = ServiceEvent

    template_name = 'project/show_event.html'

    context_object_name = 'event'

class CreateVolunteerView(CreateView):
    '''subclass of createview to add a volunteer'''

    form_class = CreateVolunteerForm

    template_name ='project/add_volunteer.html'

    #Below is test code used to debug the view
    # def form_valid(self, form):
    
    #     print(form.cleaned_data)

    #     return super().form_valid(form)

    # def form_invalid(self, form):

    #     print(form.errors)

    #     return super().form_invalid(form)

class UpdateVolunteerView(UpdateView):
    '''subclass of updateview to update a volunteer'''

    form_class=UpdateVolunteerForm

    template_name="project/update_volunteer.html"

    queryset=Volunteer.objects.all()

class DeleteVolunteerView(DeleteView):
    '''subclass of deleteview to delete a volunteer'''

    template_name = "project/delete_volunteer.html"

    queryset=Volunteer.objects.all()

    success_url="../../volunteers"
    #return to the all volunteers page upon deletion


    def get_context_data(self, **kwargs):
        '''return a dictionary with context data with which we can delete a volunteer with'''

        #use the super class to get the contxt data keyword arguments
        context= super(DeleteVolunteerView, self).get_context_data(**kwargs)

        #find the volunteer
        volunteer = Volunteer.objects.get(pk=self.kwargs["volunteer_pk"])

        #put the volunteer in the context dictionary 
        context['volunteer']=volunteer

        #return the context dictionary 
        return context

    def get_object(self):
        '''return the volunteer to be deleted'''

        #find the keyword arguments for the volunteer
        vol=self.kwargs['volunteer_pk']

        #use the pk to get the volunteer
        volunteer = Volunteer.objects.get(pk=vol)

        #return the volunteer to be deleted
        return volunteer

class CreatePartnerView(CreateView):
    '''subclass of createview to add a partner'''
    form_class =CreatePartnerForm
    template_name='project/add_partner.html'''

    #commented out the debug code from testing
    # def form_valid(self, form):

    #     print(form.cleaned_data)

    #     return super().form_valid(form)

    # def form_invalid(self, form):

    #     print(form.errors)

    #     return super().form_invalid(form)

class UpdatePartnerView(UpdateView):
    '''subclass of updateview to update a volunteer'''

    form_class=UpdatePartnerForm

    template_name="project/update_partner.html"

    queryset=CommunityPartner.objects.all()

class DeletePartnerView(DeleteView):
    '''subclass of deleteview to delete a volunteer'''

    template_name = "project/delete_partner.html"

    queryset=CommunityPartner.objects.all()

    success_url="../../partners"


    def get_context_data(self, **kwargs):
        '''return a dictionary with context data with which we can delete a partner with'''

        #create the context dictionary with the super class
        context= super(DeletePartnerView, self).get_context_data(**kwargs)

        #define the partner with the right Keyword arguments
        partner = CommunityPartner.objects.get(pk=self.kwargs["partner_pk"])

        #add the partner to the context dictionary
        context['partner']=partner

        return context

    def get_object(self):
        '''return the partner to be deleted'''

        #find the pk for the partner to be deleted
        part=self.kwargs['partner_pk']

        #define the actual partner using the pk
        partner = CommunityPartner.objects.get(pk=part)

        #return the partner to be deleted
        return partner

class CreateEventView(CreateView):
    '''subclass of createview to add an event'''
    form_class =CreateEventForm
    template_name='project/add_event.html'

    #commented out the debug code

    # def form_valid(self, form):
    
    #     print(form.cleaned_data)

    #     return super().form_valid(form)

    # def form_invalid(self, form):

    #     print(form.errors)

    #     return super().form_invalid(form)

class UpdateEventView(UpdateView):
    '''subclass of updateview to update a volunteer'''

    form_class=UpdateEventForm

    template_name="project/update_event.html"

    queryset=ServiceEvent.objects.all()

class DeleteEventView(DeleteView):
    '''subclass of deleteview to delete a volunteer'''

    template_name = "project/delete_event.html"

    queryset=ServiceEvent.objects.all()

    success_url="../../events"

    def get_context_data(self, **kwargs):
        '''return a dictionary with context data with which we can delete an event with'''

        #use the super class to create a context dictionary
        context= super(DeleteEventView, self).get_context_data(**kwargs)

        #create a variable for the event to be deleted
        event = ServiceEvent.objects.get(pk=self.kwargs["event_pk"])

        #add the event to the context dictionary
        context['event']=event

        #return the context dictionary
        return context

    def get_object(self):
        '''return the event to be deleted'''

        #store the pk for the event to be deleted
        ev =self.kwargs['event_pk']

        #track the event using the pk
        event = ServiceEvent.objects.get(pk=ev)

        #return the event to be deleted
        return event

class LandingPageView(TemplateView):
    '''subclass of templateview that will display the login'''

    template_name = 'project/landing_page.html'
    #this just displays the template to redirect to the sign in page

class HomePageView(ListView):
    '''subclass of templateview for the home page'''

    template_name = 'project/home.html'
    
    model = ServiceEvent

    context_object_name = 'event'

    #instead of creating new functions, I stored variables in the view to define the queryset
    today = today = timezone.now()

    #create a variable to create a week timeframe
    next_week = today + timedelta (7)

    #only display events that will occur in the next week on the home page
    queryset = ServiceEvent.objects.filter(service_date__gte=today).filter(service_date__lte=next_week).order_by('service_date')

class AssignVolView(DetailView):
    '''A detail view to assign vols from'''

    model = Volunteer

    template_name="project/assign_vols.html"

    context_object_name = 'volunteer'


class AssignEventView(DetailView):
    '''A detail view to assign vols from'''

    model = ServiceEvent

    template_name="project/assign_events.html"

    context_object_name = 'event'

def add_volunteer(request, volunteer_pk, event_pk):
    '''add volunteer to an event with the click of a button'''

    #comment out the debug code
    # print("volunteerpk=%s eventpk=%s" % (volunteer_pk, event_pk))
    
    #find the volunteer to be added and store it
    volunteer = Volunteer.objects.get(pk=volunteer_pk)

    #find the event to be added and store it
    event = ServiceEvent.objects.get(pk=event_pk)

    #comment out the test code
    # print("adding %s to %s" % (volunteer, event))

    #add the event to the volunteer's many to many value for events
    volunteer.service_events.add(event)

    #save the addition
    volunteer.save()

    #create a redirect url to the event's page
    url = redirect(reverse('show_event', kwargs={'pk':event_pk}))

    #return the url
    return url

def add_volunteer_return_vol(request, volunteer_pk, event_pk):
    '''add volunteer to an event with the click of a button, but return the volunteer page'''

    # comment out the test code
    # print("volunteerpk=%s eventpk=%s" % (volunteer_pk, event_pk))
    
    #find the volunteer to be added
    volunteer = Volunteer.objects.get(pk=volunteer_pk)
    
    #find the event to be added
    event = ServiceEvent.objects.get(pk=event_pk)

    #comment out the test code
    # print("adding %s to %s" % (volunteer, event))

    #add the event to the volunteer
    volunteer.service_events.add(event)

    #save the addition
    volunteer.save()

    #redirect to the volunteer's page this time
    url = redirect(reverse('show_volunteer', kwargs={'pk':volunteer_pk}))

    #return the url
    return url

def remove_volunteer(request, volunteer_pk, event_pk):
    '''remove a volunteer from an event with the click of a button'''

    #store the volunteer
    volunteer = Volunteer.objects.get(pk=volunteer_pk)

    #store the event
    event = ServiceEvent.objects.get(pk=event_pk)

    #comment out the test code
    #print("removing %s from %s" % (volunteer, event))
    
    #remove the event from the volunteer
    volunteer.service_events.remove(event)

    #save the volunteer profile
    volunteer.save()

    #create the URL
    url = redirect(reverse('show_event', kwargs={'pk':event_pk}))

    #return the URL
    return url 

def remove_volunteer_return_vol(request, volunteer_pk, event_pk):
    '''remove a volunteer from an event with the click of a button, but return the volunteer page'''

    #store the volunteer
    volunteer = Volunteer.objects.get(pk=volunteer_pk)

    #store the event
    event = ServiceEvent.objects.get(pk=event_pk)

    #comment out the test code
    #print("removing %s from %s" % (volunteer, event))
    
    #remove the event from the volunteer
    volunteer.service_events.remove(event)

    #save the removal
    volunteer.save()

    #create the url
    url = redirect(reverse('show_volunteer', kwargs={'pk':volunteer_pk}))

    #return the URL
    return url 