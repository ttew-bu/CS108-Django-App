#quotes/forms.py

from django import forms
from .models import Quote

class CreateQuoteForm(forms.ModelForm):
    '''A form to add new quotes to the db'''

    class Meta:
        '''associate this form with the Quote model.'''
        model = Quote
        fields = ['person', 'text', ] #which fields from model should inherit

class UpdateQuoteForm(forms.ModelForm):
    '''A form to update a quote to the db'''

    class Meta:
        '''assocaite this form with the Quote model'''
        model = Quote
        fields = ['person', 'text', ] #which fields model should use
