# Generated by Django 3.2.3 on 2021-05-31 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('accounts', '0001_initial'),
        ('contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('data_of_birth', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('source', models.CharField(blank=True, choices=[('Google', 'Google'), ('Facebook', 'Facebook'), ('Linkedin', 'Linkedin')], max_length=200, null=True)),
                ('assigned_to', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Lead Manager', 'Lead Manager'), ('Manager', 'Manager')], help_text='Select A Staff Member', max_length=200, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Working', 'Working'), ('Contacted', 'Contacted'), ('Proposal Sent', 'Proposal Sent'), ('Qualified', 'Qualified'), ('Customer (Converted Lead)', 'Customer (Converted Lead)'), ('Others', 'Others')], max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('accounts_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('contacts', models.ManyToManyField(to='contacts.Contact')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teams', models.ManyToManyField(to='teams.Teams')),
            ],
        ),
    ]
