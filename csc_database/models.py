from django.db import models
from django.urls import *
from datetime import *
from phonenumber_field.modelfields import *

# Create your models here.


class Volunteer(models.Model):
    '''Creates a model for a volunteer including the necessary information'''

    #Data attributes of the CSC Volunteer 
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    phone = PhoneNumberField(blank=False, max_length=13)
    email = models.EmailField(blank=False)
    bu_id = models.CharField(blank=False, max_length=9)
    class_year = models.CharField(blank=False, max_length=4)
    service_events = models.ManyToManyField('ServiceEvent', blank=True)
    
    class PrefService(models.TextChoices):
        '''Subclass to create an option set for the volunteers' focus area'''
        FOOD = 'Food Justice'
        LGBTQ = 'LGBTQ'
        Education = 'Education'
        Equity = 'Racial Equity'
        Womens = 'Empowerment of women'
    pref_service= models.CharField(max_length = 100, choices=PrefService.choices)
    
    def __str__(self):
        '''return a string representation of the Volunteer Class'''
        return '%s %s %s %s %s %s' % (self.first_name, self.last_name, self.phone, self.email, self.bu_id, self.pref_service)

    def completed_events(self):
        '''return a list of completed service events'''

        events = ServiceEvent.objects.filter(volunteer=self.pk)

        today = datetime.now(tz=timezone.utc)

        com_events = events.filter(service_date__lte=today)

        return com_events

    def incomplete_events(self):
        '''return a list of completed service events'''

        events = ServiceEvent.objects.filter(volunteer=self.pk)

        today = datetime.now(tz=timezone.utc)

        inc_events = events.filter(service_date__gte=today)

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
            
            #accumulate
            hours += event.duration

        return hours

class CommunityPartner(models.Model):
    '''Creates a model for community partners including necessary information'''
 
    #Data attributes of the CSC Community Partners
    cp_name = models.TextField(blank=False)
    cp_address = models.TextField(blank=False)
    cp_image = models.ImageField(blank=False)
    cp_mission = models.TextField(blank=False)
    cp_service_value = models.DecimalField(blank=False, max_digits=4, decimal_places=2)
    class ServiceType(models.TextChoices):
        '''Subclass to create the option set for the CP's category '''
        FOOD = 'Food Justice'
        LGBTQ = 'LGBTQ'
        Education = 'Education'
        Equity = 'Racial Equity'
        Gender = 'Gender Equity'
    cp_type= models.CharField(max_length=100, choices=ServiceType.choices)

    def __str__(self):
        '''return a string representation of the Service Event Class'''
        return '%s %s Type:%s Value:$%s' % (self.cp_name, self.cp_address, self.cp_type, self.cp_service_value)

    def events_calendar(self):
        '''Filter by pk to group all future events for a CP'''

        today = datetime.now(tz=timezone.utc)

        events = ServiceEvent.objects.filter(id=self.pk).filter(service_date__gte=today)

        return events

    def old_events(self):
        '''filter by pk to group all old events for a cp'''

        today = datetime.now(tz=timezone.utc)

        events = ServiceEvent.objects.filter(id=self.pk).filter(service_date__lte=today)

        total = len(events)

        return total

    def hours_recieved(self):
        '''calculate the hours served at a partner'''

        today = datetime.now(tz=timezone.utc)

        oldevents = ServiceEvent.objects.filter(id=self.pk).filter(service_date__lte=today)

        volunteers = Volunteer.objects.filter(service_events=self.pk)

        volunteer_qty = len(volunteers)

        hours = 0

        for event in oldevents:

            hours += event.duration * volunteer_qty

        return hours

    def monetary_equiv(self):
        '''calculate the monetary value of the total service at a partner'''

        hours = self.hours_recieved()

        money = hours * self.cp_service_value

        money_rounded = "%.2f" % (money)

        return money_rounded



        
class ServiceEvent(models.Model):
    '''Creates a model for Service Events including necessary information'''

    #Data attributes of a CSC Service Event
    event_name = models.TextField(blank=False)
    cp = models.ManyToManyField('CommunityPartner') # relationship
    event_description = models.TextField(blank=False)
    service_date = models.DateTimeField(blank=False)
    duration = models.DecimalField(blank=False, max_digits= 5, decimal_places = 2)
    capacity = models.IntegerField(blank=False)
    #volunteers =  models.ManyToManyField('Volunteer', blank=True)

    def __str__(self):
        '''return a string representation of the Service Event Class'''
        return '%s %s %s %s' % (self.event_name, self.cp, self.service_date, self.duration)

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
