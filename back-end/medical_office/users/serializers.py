# users/serializers.py
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Appointment

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'birthday', 'city', 'phone', 'assurance', 'num_assurance', 'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'user', 'date', 'time', 'type', 'comments']
