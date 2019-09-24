from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .serializers import (
    UserSerializer,
    EventSerializer,
    CompetitionSerializer,
    ContactSerializer,
    ScheduleSerializer,
)
from .models import (
    Event,
    Competition,
    Contact,
    Schedule,
)


class events(APIView):
    def get(self, request, format=None):
        users = Event.objects.all()
        serializer = EventSerializer(users, many=True)
        return Response(serializer.data)


class competitions(APIView):
    def get(self, request, format=None):
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)


class contacts(APIView):
    def get(self, requests, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class schedule(APIView):
    def get(self, requests, format=None):
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)
