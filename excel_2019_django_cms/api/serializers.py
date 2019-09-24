from rest_framework import serializers

from django.contrib.auth.models import User

from .models import(
    Event,
    Contact,
    Competition,
    CompetitionContactInfo,
    Schedule,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class EventSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    class Meta:
        model = Event
        fields = ('name', 'type', 'codename', 'website', 'details', 'img', 'created_at', 'contributor')


class CompetitionContactInfoSerializer(serializers.ModelSerializer):
    contributor =  UserSerializer()
    class Meta:
        model = CompetitionContactInfo
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    contact_numbers = CompetitionContactInfoSerializer(many=True)
    class Meta:
        model = Competition
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    class Meta:
        model = Contact
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    class Meta:
        model = Schedule
        fields = '__all__'
