# Generated by Django 2.1.4 on 2019-02-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('css_class', models.CharField(blank=True, choices=[('', 'Normal'), ('event-warning', 'Warning'), ('event-info', 'Info'), ('event-success', 'Success'), ('event-inverse', 'Inverse'), ('event-special', 'Special'), ('event-important', 'Important')], max_length=20, verbose_name='CSS Class')),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
            ],
        ),
    ]
