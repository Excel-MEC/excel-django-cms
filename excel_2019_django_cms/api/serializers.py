from rest_framework import serializers

from .models import UserClass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClass
        fields = ('user_id', )
