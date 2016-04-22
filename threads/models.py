from django.db import models
from django.conf import settings
from tinymce.models import HTMLField
from django.utils import timezone


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = HTMLField()

    def __unicode__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, related_name='threads')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
