from django.db import models
from datetime import datetime
from channels.models import Channel


class Membership(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    level = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.ImageField(upload_to='photos/membership/%Y/%m/%d/')

    def __str__(self):
        return self.title
