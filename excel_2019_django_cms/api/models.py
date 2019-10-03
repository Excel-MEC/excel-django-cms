from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
	name = models.CharField(primary_key=True,max_length=100)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
	type = models.CharField(max_length=30, null=True)
	codename = models.CharField(max_length=50, null=True)
	website = models.CharField(max_length=50, null=True)
	details = models.CharField(max_length=2000, null=True)
	img = models.ImageField(upload_to='media', null=True, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

	def __str__(self):
		return self.name + ' ' + self.type + ' ' + self.codename


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100, null=True)
	phone_number = models.CharField(max_length=100, null=True)
	img = models.ImageField(upload_to='media', null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' '


class Competition(models.Model):
	name = models.CharField(max_length=100, null=True)
	active = models.BooleanField(default=True)
	codename = models.CharField(max_length=100, null=True)
	registration = models.CharField(max_length=100, null=True)
	department = models.CharField(max_length=100, null=True)
	category = models.CharField(max_length=100, null=True)
	date = models.DateField(null=True)
	time = models.TimeField(null=True)
	venue = models.CharField(max_length=100, null=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' ' + self.codename


class CompetitionContactInfo(models.Model):
	name = models.CharField(max_length=100, null=True)
	designation = models.CharField(max_length=100, null=True)
	phone_number = models.CharField(max_length=100, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	competition = models.ForeignKey(Competition, null=True, related_name='contact_numbers', on_delete=models.CASCADE)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' ' + self.designation + ' ' + self.phone_number


class Schedule(models.Model):
	name = models.CharField(max_length=100, null=True)
	start = models.TimeField(null=True)
	end = models.TimeField(null=True)
	venue = models.CharField(max_length=100, null=True)
	department = models.CharField(max_length=100, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
