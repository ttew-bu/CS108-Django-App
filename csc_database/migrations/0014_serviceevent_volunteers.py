# Generated by Django 3.0.4 on 2020-04-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csc_database', '0013_remove_serviceevent_volunteers'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceevent',
            name='volunteers',
            field=models.ManyToManyField(blank=True, to='csc_database.Volunteer'),
        ),
    ]
