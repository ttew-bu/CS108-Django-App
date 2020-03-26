from django.db import models

# Create your models here.

class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e., text).'''

    # data attributes of a quote:
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this object **str=repr for django'''
        return '"%s" - %s' % (self.text, self.author)
