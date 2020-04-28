#forms.py
#tristan tew (ttew@bu.edu)
#Below are the necessary forms to relate submission buttons on the
#database to the models created on models.py

from django import forms
from .models import *
from phonenumber_field.formfields import * #customfield from github
from decimal import *

#service categories are used to determine volunteer interests and CP types on the forms
service_categories = [
    ('Food Justice', 'Food Justice'),
    ('LGBTQ', 'LGBTQ'),
    ('Education', 'Education'),
    ('Racial Equity', 'Racial Equity'),
    ('Empowerment of women', 'Empowerment of women'),   
]

class CreateVolunteerForm(forms.ModelForm):
    '''A form to add volunteers to the database'''

    first_name = forms.CharField(label="First Name", required=True)
    #standard character field
    last_name = forms.CharField(label="Last Name", required=True)

    phone = formfields.PhoneNumberField(label="Phone Number", required=True)
    #custom field that only works with real and validated phone numbers

    email = forms.EmailField(label="Email Address", required=True)
    #emailfield specificies what can go in here

    bu_id = forms.CharField(label="BU ID Number", required=True, max_length=9)
    #charfield allows for both numbers and letters, 9 is the length of a UID starting with U

    class_year = forms.ChoiceField(label="Class Year", choices=[(x,x) for x in range(2018,2025)], required=True)
    #use the choices in a lc to use relevant class years for volunteers

    pref_service = forms.CharField(label="Preferred Service Area", widget=forms.Select(choices=service_categories), required=True)
    #use the service categories from above so that the list lines up between models

    class Meta: #includes all fields so that the model lines up with the form
        '''associate the form with the volunteer model'''
        model = Volunteer
        fields = ['first_name', 'last_name', 'phone', 'email', 'bu_id', 'class_year', 'pref_service']

class UpdateVolunteerForm(forms.ModelForm):#all fields are the same as above because there is no reason to not change any of these fields 
    '''A form to update volunteers currently on the database'''
    first_name = forms.CharField(label="First Name", required=True)

    last_name = forms.CharField(label="Last Name", required=True)

    phone = formfields.PhoneNumberField(label="Phone Number", required=True)

    email = forms.EmailField(label="Email Address", required=True)

    bu_id = forms.CharField(label="BU ID Number", required=True, max_length=9)

    class_year = forms.ChoiceField(label="Class Year", choices=[(x,x) for x in range(2018,2025)], required=True)

    pref_service = forms.CharField(label="Preferred Service Area", widget=forms.Select(choices=service_categories), required=True)
    class Meta:
        '''associate the form with the volunteer model'''
        model = Volunteer
        fields = ['first_name', 'last_name', 'phone', 'email', 'bu_id', 'class_year', 'pref_service']

class CreatePartnerForm(forms.ModelForm):
    '''A form to add volunteers to the database'''
    cp_name = forms.CharField(label="Partner Name", required=True, help_text='Please put in the name of the CP')
    #basic Charfield

    cp_address= forms.CharField(label="Partner Address", required=True, help_text='Please put in the street address for the CP')
    #basic Charfield 

    cp_image= forms.ImageField(label="Logo", required=False, help_text='Please Attach a JPG, PNG, or other acceptable Image Format Here')
    #basic image upload

    cp_mission = forms.CharField(label="Mission", required=True, help_text='Please write a brief mission statement for the CP')
    #basic charfield since this will just display on the pages

    cp_type = forms.ChoiceField(label="Service Area", choices=service_categories, required=True, help_text='Please select the applicable service area from the list')
    #service categories line up with above form so that the models can interact

    class Meta:#includes all fields of the model to provide a clean way to put data in
        '''associate the form with the volunteer model'''
        model = CommunityPartner
        fields = ['cp_name', 'cp_address', 'cp_image', 'cp_mission', 'cp_type']

class UpdatePartnerForm(forms.ModelForm):#all of this matches the original form because there's no reason to exclude fields in the update view
    '''A form to add volunteers to the database'''
    cp_name = forms.CharField(label="Partner Name", required=True, help_text='Please put in the name of the CP')

    cp_address= forms.CharField(label="Partner Address", required=True, help_text='Please put in the street address for the CP')

    cp_image= forms.ImageField(label="Logo", required=False, help_text='Please Attach a JPG, PNG, or other acceptable Image Format Here')

    cp_mission = forms.CharField(label="Mission", required=True, help_text='Please write a brief mission statement for the CP')

    cp_type = forms.ChoiceField(label="Service Area", choices=service_categories, required=True, help_text='Please select the applicable service area from the list')

    class Meta:
        '''associate the form with the volunteer model'''
        model = CommunityPartner
        fields = ['cp_name', 'cp_address', 'cp_image', 'cp_mission', 'cp_type']

class CreateEventForm(forms.ModelForm):
    '''A form to add events to the database'''
    event_name = forms.CharField(label ="Name", required=True)
    #basic charfield for the name

    event_description = forms.CharField(label="Description", required=True)
    #basic charfield

    #duration is a decimal because events can be portions of hours; initial value is 2 because most events are a couple hours 
    duration = forms.DecimalField(label="Duration (in hours)", max_digits=4, decimal_places=2, initial=2.00, required=True)

    start_time=forms.TimeField(label="Start Time", required=True)

    service_date = forms.DateField(label="Date", widget=forms.SelectDateWidget(years=[x for x in range(2018,2030)]), required=True)

    #capacity is an integer because you cannot have half people at events. 
    capacity = forms.IntegerField(label="Capacity", required=True)

    #service value is a decimal field because currenecy needs cents and dollars. 
    service_value = forms.DecimalField(label="Service Value (in US dollars)", max_digits=5, decimal_places=2, initial=12.00, required=True)

    class Meta:#includes all parts of the model for events
        '''associate with the event model'''
        model = ServiceEvent
        fields = ['event_name', 'cp', 'event_description', 'start_time','service_date', 'duration', 'capacity', 'service_value']
    
class UpdateEventForm(forms.ModelForm):#same as the create event form so as to not exclude anything 
    '''A form to add events to the database'''
    event_name = forms.CharField(label ="Name", required=True)

    event_description = forms.CharField(label="Description", required=True)

    service_date = forms.DateField(label="Date", widget=forms.SelectDateWidget(years=[x for x in range(2018,2030)]), required=True)
    start_time=forms.TimeField(label="Start Time", required=True)

    duration = forms.DecimalField(label="Duration (in hours)", max_digits=4, decimal_places=2, initial=2.00, required=True)
    capacity = forms.IntegerField(label="Capacity", required=True)
    
    service_value = forms.DecimalField(label="Service Value (in US dollars)", max_digits=5, decimal_places=2, initial=12.00, required=True)

    class Meta:
        '''associate with the event model'''
        model = ServiceEvent
        fields = ['event_name', 'cp', 'event_description', 'service_date', 'start_time','duration', 'capacity', 'service_value']
    
