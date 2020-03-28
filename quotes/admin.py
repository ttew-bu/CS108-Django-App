from django.contrib import admin

# Register your models here.
from .models import Quote, Person, Image
admin.site.register(Quote)
admin.site.register(Person)
admin.site.register(Image)
