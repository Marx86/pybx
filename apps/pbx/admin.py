from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin, TabularInlineWithGeneric

from .models import Queue, Ivr


class BaseAdmin(GenericAdminModelAdmin):
    content_type_whitelist = ('pbx/queue', 'pbx/ivr', 'peer/subscriber')


class QueueAdmin(BaseAdmin):
    list_display = ('name', 'type', 'end')


class IvrAdmin(BaseAdmin):
    list_display = ('name', 'key0', 'key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8', 'key9', 'end')


admin.site.register(Queue, QueueAdmin)
admin.site.register(Ivr, IvrAdmin)
