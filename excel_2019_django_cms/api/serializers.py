from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class EventSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    class Meta:
        model = Event
        fields = ('name', 'type', 'codename', 'website', 'details', 'img', 'created_at', 'contributor')
