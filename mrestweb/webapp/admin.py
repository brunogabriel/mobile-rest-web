from django.contrib import admin
from models import Device

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('user', 'platform', 'device_identifier',)

# registers
admin.site.register(Device, DeviceAdmin)
