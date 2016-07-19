# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
import requests


def base_response(success=False, message='Data empty'):
	return {'success': success, 'message': message}


def obtain_token(username, password):
	if not username or not password:
		return None
	try:
		post_data = {'username': username, 'password': password}
		req = requests.post('http://localhost:8000/security/token', data=post_data)
		token = req.json()['token']
		return token
	except Exception as e:
		return None


def find_user(username, email):
	current_user = User.objects.filter(username=username).first()
	if not current_user:
		current_user = User.objects.filter(email=email).first()
	return current_user