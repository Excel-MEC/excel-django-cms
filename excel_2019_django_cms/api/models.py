from django.db import models

# Create your models here.

app_name = 'api'

class UserClass(models.Model):
	user_id = models.CharField(primary_key=True,max_length=100)
	def __str__(self):
		return self.user_id