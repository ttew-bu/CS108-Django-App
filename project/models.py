#models.py
#Tristan Tew (ttew@bu.edu)
#This file houses the three models for my CS108 final project database: Volunteers
#Community Partners, and Service Events will several methods in each to display data
#effectively on the HTML pages of this Django project. 
from django.db import models
from django.urls import *
from datetime import *
from phonenumber_field.modelfields import * #custom field I found online to create a data type just for phone numbers
import random
# Create your models here.

class Volunteer(models.Model):
    '''Creates a model for a volunteer including the necessary information'''

    #Data attributes of the CSC Volunteer 
    first_name = models.TextField(blank=False)

    last_name = models.TextField(blank=False)

    phone = PhoneNumberField(blank=False) #nomenclature is different to work with the downloaded package

    email = models.EmailField(blank=False)

    bu_id = models.CharField(blank=False, max_length=9)

    class_year = models.CharField(blank=False, max_length=4)

    service_events = models.ManyToManyField('ServiceEvent', blank=True) 
    #relationship: A volunteer can attend many events and many vols can go to many events
    
    #create a subclass to create an optionset on the eventual form and within the django admin
    class PrefService(models.TextChoices):
        '''Subclass to create an option set for the volunteers' focus area'''
        FOOD = 'Food Justice'
        LGBTQ = 'LGBTQ'
        Education = 'Education'
        Equity = 'Racial Equity'
        Womens = 'Empowerment of women'

    pref_service= models.CharField(max_length = 100, choices=PrefService.choices) 
    # actual field that tracks the preference

    def __str__(self):
        '''return a string representation of the Volunteer Class'''
        return '%s %s %s' % (self.first_name, self.last_name, self.bu_id)

    def get_absolute_url(self):
        '''Return a URL to display this volunteer object'''

        return reverse("show_volunteer", kwargs={"pk": self.pk})

    def event_list(self): 
        '''List of events for a volunteer to be added to'''

        list_ev = ServiceEvent.objects.all() # a list of all events to add a volunteer to

        return list_ev

    def completed_events(self):
        '''return a list of completed service events for one volunteer'''

        #Find all events that the volunteer has signed up for 
        events = ServiceEvent.objects.filter(volunteer=self.pk)

        #Find today's date to sort those events
        today = datetime.now(tz=timezone.utc) #set the timezone and timedate at this current moment

        #sort completed events by those that either occur today or have been completed on previous days
        com_events = events.filter(service_date__lte=today)

        #return the list of events that have been completed as of today
        return com_events

    def number_completed(self):
        '''return a number of completed service events for a vol'''

        # find completed events
        events = self.completed_events()

        # count the list
        number = len(events)

        #return the number
        return number
        
    def incomplete_events(self):
        '''return a list of completed service events'''

        #Find all events that a volunteer has signed up for, past and present
        events = ServiceEvent.objects.filter(volunteer=self.pk)

        #Find today's date to sort those events 
        today = datetime.now(tz=timezone.utc)

        #sort incomplete events by those that do not occur today or earlier
        inc_events = events.filter(service_date__gt=today)

        #return the incomplete events 
        return inc_events

    def hours_served(self):
        '''return the total number of hours served by a volunteer so far'''

        #get today's date for a point of reference
        today = datetime.now(tz=timezone.utc)

        #get the total events in a list to run through
        events = ServiceEvent.objects.filter(volunteer=self.pk).filter(service_date__lte=today)

        #set up the accumulator
        hours = 0 

        #run the accumulator pattern
        for event in events:
            
            #accumulate all hours across event by using the duration field for the event
            hours += event.duration

        # return the cumulative total of hours served
        return hours

class CommunityPartner(models.Model):
    '''Creates a model for community partners including necessary information'''
 
    #Data attributes of the CSC Community Partners
    cp_name = models.TextField(blank=False)

    cp_address = models.TextField(blank=False)

    cp_image = models.ImageField(blank=True)
    #there may be one off partners without a picture, so it is not mandatory

    cp_mission = models.TextField(blank=False)

    class ServiceType(models.TextChoices):
        '''Subclass to create the option set for the CP's category '''
        FOOD = 'Food Justice'
        LGBTQ = 'LGBTQ'
        Education = 'Education'
        Equity = 'Racial Equity'
        Womens = 'Empowerment of women'

    cp_type= models.CharField(max_length=100, choices=ServiceType.choices, blank=False)

    def __str__(self):
        '''return a string representation of the Service Event Class'''
        return '%s' % (self.cp_name)

    def get_absolute_url(self):
        '''Return a URL to display this service event object'''

        return reverse("show_partner", kwargs={"pk": self.pk})

    def past_volunteers(self):
        '''Return a list of volunteers who've served here before'''

        #find all of the old events for a partner
        events = self.old_events()

        #filter volunteers by those who attended the events in the list above and prevent repeats
        volunteers = Volunteer.objects.filter(service_events__in=events).distinct()

        #return the past volunteers
        return volunteers

    def events_calendar(self):
        '''Filter by pk to group all future events for a CP'''

        #set the time and date at the moment
        today = datetime.now(tz=timezone.utc)

        #create a queryset of events at a cp that will occur today or right now
        events = ServiceEvent.objects.filter(cp=self.pk).filter(service_date__gte=today)

        #return the queryset of events that should not be on the past calendar
        return events

    def old_events(self):
        '''Filter by pk to group all past events for a cp'''

        #set the time and date at the moment
        today = datetime.now(tz=timezone.utc)

        #create a queryset of events at a cp that have occured 
        events = ServiceEvent.objects.filter(cp=self.pk).filter(service_date__lt=today)

        #return the queryset of events that should be on the past calendar
        return events

    def sum_old_events(self):
        '''find the sum of old events at a CP'''

        #get old events
        events = self.old_events()

        #find the length of that queryset to count how many old events there were
        total = len(events)

        #return the total amount of old events
        return total

    def hours_recieved(self):
        '''calculate the hours served at a partner across all events'''

        #get the old events
        oldevents = self.old_events()

        #set accumulator variable
        hours = 0

        #create a for loop to iterate through all old events
        for event in oldevents:
            
            #the total hours served at a CP adds up for hour served per volunteer per place
            hours += event.duration * event.event_vol_count()

        #return the hours served 
        return hours

    def monetary_equiv(self):
        '''calculate the monetary value of the total service at a partner'''

        #find all of the completed events at a CP
        oldevents = self.old_events()

        #add up the monetary equivalent with a loop
        #set the accumulator variable
        dollars = 0

        #create the for loop
        for event in oldevents:
            
            #iterate
            dollars += event.event_value()

        #round the money to two decimal places for clean formatting 
        money_rounded = "%.2f" % (dollars)

        #return the rounded total
        return money_rounded

class ServiceEvent(models.Model):
    '''Creates a model for Service Events including necessary information'''

    #Data attributes of a CSC Service Event
    event_name = models.TextField(blank=False)

    cp = models.ForeignKey('CommunityPartner', on_delete=models.CASCADE, blank=False) 
    # relationship; many service events can happen at a cp, 
    # but one instance of an event can only have one cp

    event_description = models.TextField(blank=False)

    service_date = models.DateField(blank=False)#split from datetime field to display cleaner

    start_time = models.TimeField(blank=False)#split from datetime field to display cleaner

    duration = models.DecimalField(blank=False, max_digits= 5, decimal_places = 2)

    capacity = models.IntegerField(blank=False)

    service_value = models.DecimalField(blank=False, max_digits=4, decimal_places=2)

    def __str__(self):
        '''return a string representation of the Service Event Class'''
        return '%s %s' % (self.event_name, self.service_date)
    
    def get_absolute_url(self):
        '''Return a URL to display this service event object'''

        return reverse("show_event", kwargs={"pk": self.pk})

    #this is the function used on display page
    def rec_vols(self):
        '''Return a list of vols to add from'''

        #list of vols not coming to this event, this automatically will exclude those already in attendance from our query
        vol_attend = self.all_vols()

        #find the past events of the cp
        cp_ev = self.cp.old_events()

        #list of vols who have served at this cp using the previous list
        vols_cp = vol_attend.filter(service_events__in=cp_ev)

        #list of vols with matching pref service types 
        vols_list = vol_attend.filter(pref_service=self.cp.cp_type)

        #combine the lists
        all_vol = vols_cp|vols_list

        #now make it unique 
        unique_vols = all_vol.distinct()

        #return our unique list of recommendations that are not alreaedy on the event
        return unique_vols


    #this is the function used on the assign page 
    def all_vols(self):
        '''Return a list of vols to add from'''

        #excludes volunteers that are already signed up for the event
        vols = Volunteer.objects.exclude(service_events=self.pk).order_by('last_name')

        #return the list of volunteers that have not yet signed up for an event
        return vols

    def volunteer_list(self):
        '''Return the list of vols to display on the event page'''

        #return a list of vols that have this service event attached to them
        vols = Volunteer.objects.filter(service_events=self.pk)

        #return the list of volunteers that are coming to the event
        return vols

    def attendance(self):
        '''return the number of volunteers that will come to the service event'''

        #find the service event
        event = ServiceEvent.objects.get(pk=self.pk)

        #find define a list of all volunteers with matching service events
        vols = Volunteer.objects.filter(service_events=event.pk)

        #count the number of volunteers
        volunteer_count = len(vols)

        #return the count
        return volunteer_count

    def event_value(self):
        '''Calculate the total value of the service at an event'''

        #create a queryset of volunteers whose service events the current one
        volunteers = Volunteer.objects.filter(service_events=self.pk)

        #set up the accumulator variable
        dollars = 0 

        #iterate over the loop
        for volunteer in volunteers:
            
            #accumulate dollars
            dollars += self.duration * self.service_value

        #return the total dollar amount
        return dollars

    def event_vol_count(self):
        '''calculate the total vols per event'''
        
        #find all volunteers at this event
        vols = Volunteer.objects.filter(service_events=self.pk)

        #Count the number of people at the event
        num_vols = len(vols)

        #return the sum of people
        return num_vols
