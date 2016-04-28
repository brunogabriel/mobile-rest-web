# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
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

	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
	platform = models.CharField(max_length=3, choices=DEVICE_PLATFORMS, default=ANDROID, verbose_name='Platform')
	device_identifier = models.CharField(max_length=64, unique=True, verbose_name='Identifier')

	def __str__(self):
		return '%s' % (self.device_identifier)

	class Meta:
		verbose_name = 'User device'
		verbose_name_plural = 'User devices'

