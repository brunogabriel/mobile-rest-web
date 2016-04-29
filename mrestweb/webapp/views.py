
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.views import exception_handler
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from forms import *
from util import *
import requests
import json


@api_view(['POST'])
def do_login(request):
	try:
		form = LoginForm(request.POST)
		if form.is_valid():
			return JsonResponse(form.handle(request=request))
		else:
			JsonResponse(base_response(False, 'Problem to login, verify your credentials and try again.'))
	except Exception as e:
		return JsonResponse(base_response(False, 'Error during login, verify your network connection or try again later.'))
