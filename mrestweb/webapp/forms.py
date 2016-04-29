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
				raise Exception('Invalid user credentials.')
			
			user = Token.objects.get(key=token).user
			user_serializer = UserSerializer(user)
			
			response = base_response(True, 'Success to login.')
			response['user'] = user_serializer.data
			response['user']['token'] = token
			
			return response
		except Exception as e:
			return base_response(False, 'Fail to login.')


class CreateAccountForm(forms.Form):
	firstname = forms.CharField(required=True)
	lastname = forms.CharField(required=True)
	username = forms.CharField(required=True)
	email = forms.CharField(required=True)
	password = forms.CharField(required=True)

	def handle(self, request=None):
		try:
			firstname =  self.cleaned_data['firstname']
			lastname =  self.cleaned_data['lastname']
			username =  self.cleaned_data['username']
			email =  self.cleaned_data['email']
			password = self.cleaned_data['password']

			# Try to get User
			user = find_user(username, email)

			if user:
				return base_response(False, 'This account exists, try other credentials.')

			delete_error = True
			current_user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname, is_staff=True)
			current_user.save()
			
			# If you need to permit user login in admin, I think that its necessary to add the created user to a group
			# group = Group.objects.filter(name='<groupname>').first()
			# if group: group.user_set.add(current_user)
			
			return base_response(True, 'Welcome')
		except Exception as e:
			if delete_error:
				try:
					current_user.delete()
				except:
					pass
			print str(e)
			return base_response(False, 'Fail to create account.')
