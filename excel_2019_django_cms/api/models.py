from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class UserClass(models.Model):
	user_id = models.CharField(primary_key=True,max_length=100)
	def __str__(self):
		return self.user_id


class Event(models.Model):
	name = models.CharField(primary_key=True,max_length=100)
	contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, related_name='contributor')
	type = models.CharField(max_length=30)
	codename = models.CharField(max_length=50)
	website = models.CharField(max_length=50)
	details = models.CharField(max_length=2000)
	img = models.ImageField(upload_to='media')
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.name + ' ' + self.type + ' ' + self.codename
