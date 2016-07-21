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
	platform = forms.CharField(required=False)
	device_identifier = forms.CharField(required=False)

	def handle(self, request=None):
		try:
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			platform = self.cleaned_data['platform']
			device_identifier = self.cleaned_data['device_identifier']

			if platform not in ['AND', 'IOS', 'WPH'] or not device_identifier:
				raise Exception('Invalid platform, check your credentials.')
			
			token = obtain_token(username, password)
			if not token:
				raise Exception('Invalid user credentials.')

			user = Token.objects.get(key=token).user
			user_serializer = UserSerializer(user)
			device_user = Device.objects.filter(user=user, platform=platform, device_identifier=device_identifier).first()

			if device_user:
				print 'User already has device platform'
			else:
				device_user = Device(user=user, platform=platform, device_identifier=device_identifier)
				device_user.save()
			response = base_response(True, 'Success to login.')
			response['user'] = user_serializer.data
			response['user']['token'] = token
			
			return response
		except Exception as e:
			return base_response(False, 'Fail to login, verify your data.')


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
			
			return base_response(True, ' '.join['Welcome', firstname])
		except Exception as e:
			if delete_error:
				try:
					current_user.delete()
				except:
					pass
			print str(e)
			return base_response(False, 'Fail to create account.')

class TeamsPagination(forms.Form):
	token = forms.CharField(required=True)
	username = forms.CharField(required=True)
	init = forms.IntegerField(required=False)
	threshould = forms.IntegerField(required=False)

	def clean(self):
		cleaned_data = super(TeamsPagination, self).clean()
		for key, value in cleaned_data.items():
			if not value:
				cleaned_data[key] = self.initial[key]
		return cleaned_data

	def handle(self, request=None):
		token = self.cleaned_data['token']
		username =  self.cleaned_data['username']
		init = self.cleaned_data['init']
		threshould = self.cleaned_data['threshould']

		valid_user = Token.objects.filter(key=token, user__username=username).first()
		if not valid_user:
				return base_response(False, 'Invalid credentials.')

		teams = Team.objects.all().order_by('id')[init:init+threshould]
		teams_serializer = TeamSerializer(teams, many=True)

		response = base_response(True, 'Success on list teams')
		response['teams'] = teams_serializer.data

		return response



