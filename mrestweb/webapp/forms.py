# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from models import *
from serializers import *
from util import *


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)

	def handle(self, request=None):
		try:
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			
			token = obtain_token(username, password)
			if not token:
				raise Exception('Invalid user credentials')
			
			user = Token.objects.get(key=token).user
			user_serializer = UserSerializer(user)
			
			response = base_response(True, 'Success to login.')
			response['user'] = user_serializer.data
			response['user']['token'] = token
			
			return response
		except Exception as e:
			return base_response(False, 'Fail to login.')