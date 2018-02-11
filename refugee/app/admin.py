from django.contrib import admin
from .models import Refugee, NGO, NgoPetition, NgoPetitionVote, Notification, Event, RefugeePetition
from .models import RefugeePetitionVote


admin.site.register(Refugee)
admin.site.register(NGO)
admin.site.register(Notification)
admin.site.register(NgoPetition)
admin.site.register(NgoPetitionVote)
admin.site.register(Event)
admin.site.register(RefugeePetition)
admin.site.register(RefugeePetitionVote)
