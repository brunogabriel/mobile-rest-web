# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	""" Automatically creates a token to all created users """
	if created:
		Token.objects.create(user=instance)


@python_2_unicode_compatible
class Device(models.Model):
	ANDROID = 'AND'
	IOS = 'IOS'
	WINDOWS_PHONE = 'WPH'

	DEVICE_PLATFORMS = (
		(ANDROID, 'Android'),
		(IOS, 'iOS'),
		(WINDOWS_PHONE, 'Windows Phone')
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
	platform = models.CharField(max_length=3, choices=DEVICE_PLATFORMS, default=ANDROID, verbose_name='Platform')
	device_identifier = models.CharField(max_length=64, unique=True, verbose_name='Identifier')

	def __str__(self):
		return '%s' % (self.device_identifier)

	class Meta:
		verbose_name = 'User device'
		verbose_name_plural = 'User devices'


@python_2_unicode_compatible
class Team(models.Model):
	EASTERN_CONFERENCE = 'EC'
	WESTERN_CONFERENCE ='WC'
	CONFERENCES = (
		(EASTERN_CONFERENCE, 'EASTERN'),
		(WESTERN_CONFERENCE, 'WESTERN')
	)

	name = models.CharField(max_length=64, verbose_name='Name')
	conference = models.CharField(max_length=2, choices=CONFERENCES, default=EASTERN_CONFERENCE, verbose_name='Conference')
	arena = models.CharField(max_length=64, verbose_name='Arena')
	foundation = models.DateField(verbose_name='Foundation')
	about_history = models.TextField(verbose_name='About/History')
	flag = models.TextField(validators=[URLValidator()], verbose_name='Flag')

	def thumbnail(self):
		return '<img src="%s" style="max-width: 40px;  max-height: 40px;">' % self.flag
	thumbnail.allow_tags = True
	thumbnail.short_description = 'Thumbnail'

	def __str__(self):
		return '%s' % (self.name)

	class Meta:
		verbose_name = 'Team'
		verbose_name_plural = 'Teams'



