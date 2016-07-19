# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email', )