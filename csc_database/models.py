from django.db import models
from django.urls import *
from phonenumber_field.modelfields import *
# Create your models here.


class Volunteer(models.Model):
    '''Creates a model for a volunteer including the necessary information'''

    #Data attributes of the CSC Volunteer 
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    phone = PhoneNumberField(blank=False)
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

        return events

    def hours_served(self):
        '''return the total number of hours served by a volunteer so far'''

        #get the total events in a list to run through
        events = ServiceEvent.objects.filter(volunteer=self.pk)

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
        '''Filter by pk to group all events for a CP'''

        events = ServiceEvent.objects.filter(id=self.pk)

        return events

class ServiceEvent(models.Model):
    '''Creates a model for Service Events including necessary information'''

    #Data attributes of a CSC Service Event
    event_name = models.TextField(blank=False)
    cp = models.OneToOneField(CommunityPartner, on_delete=models.CASCADE) # relationship
    event_description = models.TextField(blank=False)
    service_date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    duration = models.DecimalField(blank=False, max_digits= 5, decimal_places = 2)
    #capacity = models.IntegerField(blank=True, max=100)
    #spots_remaining = 
    def __str__(self):
        '''return a string representation of the Service Event Class'''
        return '%s %s %s Start:%s Duration:%s' % (self.event_name, self.cp.cp_name, self.service_date, self.start_time, self.duration)
