from django.shortcuts import render
from .models import *
from django.views.generic import *
from .forms import * 
from django.shortcuts import *
from django.urls import *

# Create your views here.

class ShowAllCommunityPartnersView(ListView):
    '''subclass of listview that displays all CPs'''
    model = CommunityPartner
    template_name= 'csc_database/all_partners.html'
    context_object_name = 'all_partners'
    queryset = CommunityPartner.objects.all().order_by('cp_name')

class ShowCommunityPartnerPageView(DetailView):
    '''subclass of detailview for info on one cp'''
    model = CommunityPartner
    template_name = 'csc_database/show_partner.html'
    context_object_name = 'partner'

class ShowAllVolunteersView(ListView):
    '''subclass of listview to display all volunteers'''
    model = Volunteer
    template_name = 'csc_database/all_volunteers.html'
    context_object_name = 'all_volunteers'
    queryset=Volunteer.objects.all().order_by('bu_id')

class ShowVolunteerPageView(DetailView):
    '''subclass of detailview to show an individual volunteer's information'''
    model = Volunteer
    template_name = 'csc_database/show_volunteer.html'
    context_object_name = 'volunteer'

class ShowAllEventsView(ListView):
    '''subclass of listview to display all Events'''
    model = ServiceEvent
    template_name = 'csc_database/all_events.html'
    context_object_name = 'all_events'
    queryset = ServiceEvent.objects.all().order_by('service_date')

class ShowEventPageView(DetailView):
    '''subclass of detailview to show an individual volunteer's information'''
    model = ServiceEvent
    template_name = 'csc_database/show_event.html'
    context_object_name = 'event'

class CreateVolunteerView(CreateView):
    '''subclass of createview to add a volunteer'''
    form_class =CreateVolunteerForm
    template_name ='csc_database/add_volunteer.html'

    def form_valid(self, form):
    
        print(form.cleaned_data)

        return super().form_valid(form)

    def form_invalid(self, form):

        print(form.errors)

        return super().form_invalid(form)

class UpdateVolunteerView(UpdateView):
    '''subclass of updateview to update a volunteer'''
    form_class=UpdateVolunteerForm
    template_name="csc_database/update_volunteer.html"
    queryset=Volunteer.objects.all()

class DeleteVolunteerView(DeleteView):
    '''subclass of deleteview to delete a volunteer'''
    template_name = "csc_database/delete_volunteer.html"
    queryset=Volunteer.objects.all()
    success_url="../../volunteers"


    def get_context_data(self, **kwargs):
        '''return a dictionary with context data with which we can delete a partner with'''

        context= super(DeleteVolunteerView, self).get_context_data(**kwargs)

        volunteer = Volunteer.objects.get(pk=self.kwargs["volunteer_pk"])

        context['volunteer']=volunteer

        return context

    def get_object(self):
        '''return the partner to be deleted'''
        vol=self.kwargs['volunteer_pk']

        volunteer = Volunteer.objects.get(pk=vol)

        return volunteer

class CreatePartnerView(CreateView):
    '''subclass of createview to add a partner'''
    form_class =CreatePartnerForm
    template_name='csc_database/add_partner.html'''


    def form_valid(self, form):

        print(form.cleaned_data)

        return super().form_valid(form)

    def form_invalid(self, form):

        print(form.errors)

        return super().form_invalid(form)

class UpdatePartnerView(UpdateView):
    '''subclass of updateview to update a volunteer'''
    form_class=UpdatePartnerForm
    template_name="csc_database/update_partner.html"
    queryset=CommunityPartner.objects.all()

class DeletePartnerView(DeleteView):
    '''subclass of deleteview to delete a volunteer'''
    template_name = "csc_database/delete_partner.html"
    queryset=CommunityPartner.objects.all()
    success_url="../../partners"


    def get_context_data(self, **kwargs):
        '''return a dictionary with context data with which we can delete a partner with'''

        context= super(DeletePartnerView, self).get_context_data(**kwargs)

        partner = CommunityPartner.objects.get(pk=self.kwargs["partner_pk"])

        context['partner']=partner

        return context

    def get_object(self):
        '''return the partner to be deleted'''
        part=self.kwargs['partner_pk']

        partner = CommunityPartner.objects.get(pk=part)

        return partner

class CreateEventView(CreateView):
    '''subclass of createview to add an event'''
    form_class =CreateEventForm
    template_name='csc_database/add_event.html'

    def form_valid(self, form):
    
        print(form.cleaned_data)

        return super().form_valid(form)

    def form_invalid(self, form):

        print(form.errors)

        return super().form_invalid(form)

class UpdateEventView(UpdateView):
    '''subclass of updateview to update a volunteer'''
    form_class=UpdateEventForm
    template_name="csc_database/update_event.html"
    queryset=ServiceEvent.objects.all()

class DeleteEventView(DeleteView):
    '''subclass of deleteview to delete a volunteer'''
    template_name = "csc_database/delete_event.html"
    queryset=ServiceEvent.objects.all()
    success_url="../../events"


    def get_context_data(self, **kwargs):
        '''return a dictionary with context data with which we can delete an event with'''

        context= super(DeleteEventView, self).get_context_data(**kwargs)

        event = ServiceEvent.objects.get(pk=self.kwargs["event_pk"])

        context['event']=event

        return context

    def get_object(self):
        '''return the event to be deleted'''
        ev =self.kwargs['event_pk']

        event = ServiceEvent.objects.get(pk=ev)

        return event

class LandingPageView(TemplateView):
    '''subclass of templateview that will display the login'''
    template_name = 'csc_database/landing_page.html'

class HomePageView(ListView):
    '''subclass of templateview for the home page'''
    template_name = 'csc_database/home.html'
    model = ServiceEvent
    context_object_name = 'event'
    today = datetime.today()
    next_week = datetime.today() + timedelta(7)
    queryset = ServiceEvent.objects.filter(service_date__gte=today).filter(service_date__lte=next_week).order_by('service_date')

class AssignVolView(DetailView):
    '''A detail view to assign vols from'''
    model = Volunteer
    template_name="csc_database/assign_vols.html"
    context_object_name = 'volunteer'


class AssignEventView(DetailView):
    '''A detail view to assign vols from'''
    model = ServiceEvent
    template_name="csc_database/assign_events.html"
    context_object_name = 'event'

def add_volunteer(request, volunteer_pk, event_pk):
    '''add volunteer to an event with the click of a button'''
    print("volunteerpk=%s eventpk=%s" % (volunteer_pk, event_pk))
    
    volunteer = Volunteer.objects.get(pk=volunteer_pk)
    
    event = ServiceEvent.objects.get(pk=event_pk)
    print("adding %s to %s" % (volunteer, event))
    volunteer.service_events.add(event)

    volunteer.save()

    url = redirect(reverse('show_event', kwargs={'pk':event_pk}))

    return url

def remove_volunteer(request, volunteer_pk, event_pk):
    '''remove a volunteer from an event with the click of a button'''

    volunteer = Volunteer.objects.get(pk=volunteer_pk)

    event = ServiceEvent.objects.get(pk=event_pk)

    print("removing %s from %s" % (volunteer, event))
    
    volunteer.service_events.remove(event)

    volunteer.save()

    url = redirect(reverse('show_event', kwargs={'pk':event_pk}))

    return url 