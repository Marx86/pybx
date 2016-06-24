from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from apps.peer.models import Subscriber


class Queue(models.Model):
    QUEUE_TYPES = (
        ('all', _('Call to all subscribers')),
        ('random', _('Random')),
    )

    name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(Subscriber)
    type = models.CharField(choices=QUEUE_TYPES, max_length=32)
    moh = models.FileField(upload_to='moh')
    waiting = models.DurationField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, default=None, blank=True)
    object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    end = GenericForeignKey()

    def __repr__(self):
        return u'{}: {}'.format(_('Queue'), self.name)


class Ivr(models.Model):
    name = models.CharField(max_length=255)
    greeting = models.FileField(upload_to='ivr')
    waiting = models.DurationField()
    attempts = models.PositiveIntegerField()
    key0_content_type = models.ForeignKey(ContentType, related_name='key0_content_type', null=True,
                                          default=None, blank=True, on_delete=models.CASCADE)
    key0_object_id = models.PositiveIntegerField()
    key0 = GenericForeignKey('key0_content_type', 'key0_object_id')
    key1_content_type = models.ForeignKey(ContentType, related_name='key1_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key1_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key1 = GenericForeignKey('key1_content_type', 'key1_object_id')
    key2_content_type = models.ForeignKey(ContentType, related_name='key2_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key2_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key2 = GenericForeignKey('key2_content_type', 'key2_object_id')
    key3_content_type = models.ForeignKey(ContentType, related_name='key3_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key3_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key3 = GenericForeignKey('key3_content_type', 'key3_object_id')
    key4_content_type = models.ForeignKey(ContentType, related_name='key4_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key4_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key4 = GenericForeignKey('key4_content_type', 'key4_object_id')
    key5_content_type = models.ForeignKey(ContentType, related_name='key5_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key5_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key5 = GenericForeignKey('key5_content_type', 'key5_object_id')
    key6_content_type = models.ForeignKey(ContentType, related_name='key6_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key6_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key6 = GenericForeignKey('key6_content_type', 'key6_object_id')
    key7_content_type = models.ForeignKey(ContentType, related_name='key7_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key7_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key7 = GenericForeignKey('key7_content_type', 'key7_object_id')
    key8_content_type = models.ForeignKey(ContentType, related_name='key8_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key8_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key8 = GenericForeignKey('key8_content_type', 'key8_object_id')
    key9_content_type = models.ForeignKey(ContentType, related_name='key9_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    key9_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    key9 = GenericForeignKey('key9_content_type', 'key9_object_id')
    end_content_type = models.ForeignKey(ContentType, related_name='end_content_type', null=True, default=None, blank=True, on_delete=models.CASCADE)
    end_object_id = models.PositiveIntegerField(null=True, default=None, blank=True)
    end = GenericForeignKey('end_content_type', 'end_object_id')

    def __repr__(self):
        return u'{}: {}'.format(_('IVR'), self.name)
