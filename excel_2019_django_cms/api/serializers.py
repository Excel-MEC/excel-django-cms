from rest_framework import serializers

from django.contrib.auth.models import User

from .models import(
    Event,
    Contact,
    Competition,
    CompetitionContactInfo,
    Schedule,
    EventContactInfo,
    EventButton,
    CompetitionButton
)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'email')


class EventContactInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventContactInfo
        fields = '__all__'


class EventButtonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventButton
        fields = ('name', 'link')


class EventSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    contact_numbers = EventContactInfoSerializer(many=True)
    buttons = EventButtonSerializer(many=True)
    
    class Meta:
        model = Event
        fields = '__all__'


class CompetitionContactInfoSerializer(serializers.ModelSerializer):
    contributor =  UserSerializer()
    
    class Meta:
        model = CompetitionContactInfo
        fields = '__all__'

class CompetitionButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompetitionButton
        fields = ('name', 'link')


class CompetitionSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    contact_numbers = CompetitionContactInfoSerializer(many=True)
    buttons = CompetitionButtonSerializer(many=True)
    
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
