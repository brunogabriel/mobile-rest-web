from django.contrib import admin
from models import Device
from models import Team

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('user', 'platform', 'device_identifier',)

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'conference', 'arena', 'foundation', 'thumbnail',)


# registers
admin.site.register(Device, DeviceAdmin)
admin.site.register(Team, TeamAdmin)
