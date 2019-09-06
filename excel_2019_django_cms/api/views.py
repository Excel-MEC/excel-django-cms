from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import UserClass


class index(APIView):
    def get(self, request, format=None):
        users = UserClass.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)