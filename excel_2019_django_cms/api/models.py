from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
	name = models.CharField(primary_key=True,max_length=100)
	codename = models.CharField(max_length=50, null=True, blank=True)
	img = models.CharField(max_length=100, null=True, blank=True)
	# img = models.ImageField(upload_to='media', null=True)
	description = models.TextField(null=True, blank=True)
	info = models.TextField(blank=True, null=True)
	type = models.CharField(max_length=30, null=True, blank=True)
	website = models.CharField(max_length=50, null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' ' + self.type + ' ' + self.codename


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100, null=True, blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)
	img = models.CharField(max_length=100, null=True, blank=True)
	# img = models.ImageField(upload_to='media', null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' ' + self.email


class Competition(models.Model):
	name = models.CharField(max_length=100, null=True)
	img = models.CharField(max_length=100, null=True, blank=True)
	# img = models.ImageField(upload_to='media', null=True, blank=True)
	codename = models.CharField(max_length=100, null=True, blank=True)
	venue = models.CharField(max_length=100, null=True, blank=True)
	# date = models.DateField(null=True, blank=True)
	# time = models.TimeField(null=True, blank=True)
	date = models.CharField(max_length=100, null=True, blank=True)
	time = models.CharField(max_length=100, null=True, blank=True)
	format = models.TextField(null=True, blank=True)
	rules = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	category = models.CharField(max_length=100, null=True, blank=True)
	type = models.CharField(max_length=100, null=True, blank=True)
	about = models.TextField(null=True, blank=True)
	prize = models.CharField(max_length=100, null=True, blank=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' ' + self.codename


class CompetitionContactInfo(models.Model):
	name = models.CharField(max_length=100, null=True)
	designation = models.CharField(max_length=100, null=True, blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	competition = models.ForeignKey(Competition, null=True, related_name='contact_numbers', on_delete=models.CASCADE, blank=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' ' + self.designation + ' ' + self.phone_number


class CompetitionButton(models.Model):
	name = models.CharField(max_length=100, null=True)
	link = models.CharField(max_length=100, null=True)
	Competition = models.ForeignKey(Competition, null=True, related_name='buttons', on_delete=models.CASCADE)


class EventContactInfo(models.Model):
	name = models.CharField(max_length=100, null=True)
	designation = models.CharField(max_length=100, null=True, blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	event = models.ForeignKey(Event, null=True, related_name='contact_numbers', on_delete=models.CASCADE)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	def __str__(self):
		return self.name + ' ' + self.designation + ' ' + self.phone_number


class EventButton(models.Model):
	name = models.CharField(max_length=100, null=True)
	link = models.CharField(max_length=100, null=True)
	event = models.ForeignKey(Event, null=True, related_name='buttons', on_delete=models.CASCADE)


class Schedule(models.Model):
	name = models.CharField(max_length=100, null=True)
	venue = models.CharField(max_length=100, null=True, blank=True)
	codename = models.CharField(max_length=100, null=True, blank=True)
	# date = models.DateField(null=True)
	# time = models.TimeField(null=True)
	date = models.CharField(max_length=100, null=True, blank=True)
	time = models.CharField(max_length=100, null=True, blank=True)
	img = models.CharField(max_length=100, null=True, blank=True)
	# img = models.ImageField(upload_to='media', null=True, blank=True)
	day = models.IntegerField(default=1)
	category = models.CharField(max_length=100, null=True, blank=True)
	daytime = models.CharField(max_length=100, null=True, choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], blank=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

	class Meta:
		verbose_name_plural = 'Schedule'

	def __str__(self):
		return self.name + ' ' + self.category

