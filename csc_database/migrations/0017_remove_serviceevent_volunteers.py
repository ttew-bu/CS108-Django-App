# Generated by Django 3.0.4 on 2020-04-16 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csc_database', '0016_auto_20200415_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceevent',
            name='volunteers',
        ),
    ]