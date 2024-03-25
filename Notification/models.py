from django.db import models

# Create your models here.
class UserDevice(models.Model):
    user = models.CharField(max_length=100)
    subscription = models.JSONField(null=True, blank=True)