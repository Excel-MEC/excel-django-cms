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
	img = models.ImageField(upload_to='media, null=True', null=True)
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

'''
Contacts

"username": "georgeshanti",
"email": "georgeshanti@gmail.com",
"id": 1,
"createdAt": "2018-10-02T10:11:56.737Z",
"updatedAt": "2018-10-16T14:17:31.252Z"

Competition
"active": true,
"name": "Third Eye Photography",
"codename": "third-eye",
"contactInfo": [
	{
	"name": "Tinu Mathew",
	"designation": "Event Coordinator",
	"phone": "+91 97467 75597"
	},
	{
	"name": "Atul Krishnan",
	"designation": "Event Coordinator",
	"phone": "+91 95441 20630"
	}
],
"registration": "No Additional Fee",
"department": "Non-Tech",
"category": "Online",
"date": "--",
"time": "--",
"venue": "Govt. Model Engineering College, Thrikkakara",
"img": "http://excelmec.org/static/images/third-eye-photography.png",
"color": "#2fb454",
"id": 1

Sponsors
"createdAt": "2018-11-01T18:26:24.245Z",
"color": "#fff",
"name": "Nest Technologies",
"category": "Title Sponsor",
"link": "http://nesttech.com/",
"img": "https://excelmec.org/static/media/nest_logo.62648bc1.png",
"updatedAt": "2018-11-01T18:33:45.040Z",
"id": 1
'''