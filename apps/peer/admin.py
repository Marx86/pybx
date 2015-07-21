from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'callerid')

admin.site.register(Subscriber, SubscriberAdmin)
