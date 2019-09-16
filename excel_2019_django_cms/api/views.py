from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .serializers import UserSerializer, EventSerializer
from .models import Event


class events(APIView):
    def get(self, request, format=None):
        users = Event.objects.all()
        serializer = EventSerializer(users, many=True)
        return Response(serializer.data)