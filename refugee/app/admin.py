from django.contrib import admin
from .models import Refugee, NGO, NgoPetition, NgoPetitionVote


admin.site.register(Refugee)
admin.site.register(NGO)
admin.site.register(NgoPetition)
admin.site.register(NgoPetitionVote)
