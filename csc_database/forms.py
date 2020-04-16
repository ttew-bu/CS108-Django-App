#forms.py
#tristan tew (ttew@bu.edu)
#Below are the necessary forms to relate submission buttons on the
#database to the models created on models.py

from django import forms
from .models import *
from phonenumber_field.formfields import *

service_categories = [
    ('Food Justice', 'Food Justice'),
    ('LGBTQ', 'LGBTQ'),
    ('Education', 'Education'),
    ('Racial Equity', 'Racial Equity'),
    ('Female Empowerment', 'Empowerment of women'),   
]

class CreateVolunteerForm(forms.ModelForm):
    '''A form to add volunteers to the database'''
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    phone = formfields.PhoneNumberField(label="Phone Number", required=True)
    email = forms.EmailField(label="Email Address", required=True)
    bu_id = forms.CharField(label="BU ID Number", required=True, max_length=9)
    class_year = forms.IntegerField(label="Class Year", required=True, min_value=2018, max_value=2100)
    pref_service= forms.MultipleChoiceField(label="Preferred Service Areas", choices=service_categories, widget=forms.CheckboxSelectMultiple, required=True)

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
    cp_service_value = forms.CharField(label="Service Value", required=True, max_length=9, help_text='Please write in the value of service to 2 decimal points (e.g. 12.00)')
    cp_type = forms.MultipleChoiceField(label="Service Area", choices=service_categories, widget=forms.RadioSelect, required=True, help_text='Please select the applicable service area from the list')

    class Meta:
        '''associate the form with the volunteer model'''
        model = CommunityPartner
        fields = ['cp_name', 'cp_address', 'cp_image', 'cp_mission', 'cp_service_value', 'cp_type']