from django.db import models

#file: models.py
#author: Tristan Tew (ttew@bu.edu)
#description: creating the model for the profile to display on mini_fb

# Create your models here.

#This model 

class Profile(models.Model):
    '''Creates the format for the profile model'''

    #data attributes of a mini_fb profile:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)

    #create a string representation of the 

    def __str__(self):
        '''return a string representation of this object'''
        return '%s %s %s %s' % (self.first_name, self.last_name, self.city, self.email_address)