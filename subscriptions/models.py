from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from channels.models import Channel


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    level = models.IntegerField()
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    payment_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.user)
