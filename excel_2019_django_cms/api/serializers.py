from rest_framework import serializers

from .models import UserClass, Event
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class EventSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    class Meta:
        model = Event
        fields = ('name', 'type', 'codename', 'website', 'details', 'img', 'created_at', 'contributor')
