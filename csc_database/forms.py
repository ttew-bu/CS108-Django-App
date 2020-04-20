#forms.py
#tristan tew (ttew@bu.edu)
#Below are the necessary forms to relate submission buttons on the
#database to the models created on models.py

from django import forms
from .models import *
from phonenumber_field.formfields import *
from decimal import *

service_categories = [
    ('Food Justice', 'Food Justice'),
    ('LGBTQ', 'LGBTQ'),
    ('Education', 'Education'),
    ('Racial Equity', 'Racial Equity'),
    ('Female Empowerment', 'Empowerment of women'),   
]
class_years = [int for int in range(2018,2030)]

class CreateVolunteerForm(forms.ModelForm):
    '''A form to add volunteers to the database'''
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

class UpdateVolunteerForm(forms.ModelForm):
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
    cp_address= forms.CharField(label="Partner Address", required=True, help_text='Please put in the street address for the CP')
    cp_image= forms.ImageField(label="Logo", required=True, help_text='Please Attach a JPG, PNG, or other acceptable Image Format Here')
    cp_mission = forms.CharField(label="Mission", required=True, help_text='Please write a brief mission statement for the CP')
    cp_type = forms.ChoiceField(label="Service Area", choices=service_categories, required=True, help_text='Please select the applicable service area from the list')

    class Meta:
        '''associate the form with the volunteer model'''
        model = CommunityPartner
        fields = ['cp_name', 'cp_address', 'cp_image', 'cp_mission', 'cp_type']

class UpdatePartnerForm(forms.ModelForm):
    '''A form to add volunteers to the database'''
    cp_name = forms.CharField(label="Partner Name", required=True, help_text='Please put in the name of the CP')
    cp_address= forms.CharField(label="Partner Address", required=True, help_text='Please put in the street address for the CP')
    cp_image= forms.ImageField(label="Logo", required=True, help_text='Please Attach a JPG, PNG, or other acceptable Image Format Here')
    cp_mission = forms.CharField(label="Mission", required=True, help_text='Please write a brief mission statement for the CP')
    cp_type = forms.ChoiceField(label="Service Area", choices=service_categories, required=True, help_text='Please select the applicable service area from the list')

    class Meta:
        '''associate the form with the volunteer model'''
        model = CommunityPartner
        fields = ['cp_name', 'cp_address', 'cp_image', 'cp_mission', 'cp_type']

class CreateEventForm(forms.ModelForm):
    '''A form to add events to the database'''
    event_name = forms.CharField(label ="Name", required=True)
    event_description = forms.CharField(label="Description", required=True)
    duration = forms.DecimalField(label="Duration (in hours)", max_digits=4, decimal_places=2, initial=2.00, required=True)
    capacity = forms.IntegerField(label="Capacity", required=True)
    service_value = forms.DecimalField(label="Service Value (in US dollars)", max_digits=5, decimal_places=2, initial=12.00, required=True)

    class Meta:
        '''associate with the event model'''
        model = ServiceEvent
        fields = ['event_name', 'cp', 'event_description', 'service_date', 'duration', 'capacity', 'service_value']
    
class UpdateEventForm(forms.ModelForm):
    '''A form to add events to the database'''
    event_name = forms.CharField(label ="Name", required=True)
    event_description = forms.CharField(label="Description", required=True)
    duration = forms.DecimalField(label="Duration (in hours)", max_digits=4, decimal_places=2, initial=2.00, required=True)
    capacity = forms.IntegerField(label="Capacity", required=True)
    service_value = forms.DecimalField(label="Service Value (in US dollars)", max_digits=5, decimal_places=2, initial=12.00, required=True)

    class Meta:
        '''associate with the event model'''
        model = ServiceEvent
        fields = ['event_name', 'cp', 'event_description', 'service_date', 'duration', 'capacity', 'service_value']
    
