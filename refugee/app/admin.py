from django.contrib import admin
from .models import Refugee, NGO, Notification


admin.site.register(Refugee)
admin.site.register(NGO)
admin.site.register(Notification)
