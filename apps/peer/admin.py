from django.contrib import admin
from .models import Peer, Subscriber


class PeerAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'callerid')
    standard_fields = ('name', 'username', 'callerid', 'type', 'allow', 'secret')
    exclude = ('is_peer', 'user')

    def __init__(self, model, *args, **kwargs):
        super(PeerAdmin, self).__init__(model, *args, **kwargs)

        fields = [f.name for f in model._meta.fields if f.name != 'id']

        self.fieldsets = (
            (
                'Standard settings', {
                    'fields': self.standard_fields
                }
            ),
            (
                'Advanced settings', {
                    'fields': list(set(fields) - set(self.exclude) - set(self.standard_fields))
                }
            ),
        )


class SubscriberAdmin(PeerAdmin):
    standard_fields = ('user', 'name', 'username', 'callerid', 'type', 'allow', 'secret')
    exclude = ('is_peer',)


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Peer, PeerAdmin)
