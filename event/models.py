from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime

class Eventtype(models.Model):
    eventtype = models.CharField(max_length=200)

    def __str__(self):
        return self.eventtype

class Organizer(models.Model):
    eventorganizer = models.CharField(max_length=200)

    def __str__(self):
        return self.eventorganizer

class Eventlocation(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

class Event(models.Model):
    eventname = models.CharField(max_length=200,verbose_name= "Event Name")
    eventdescription = models.CharField(max_length=300, verbose_name= "Event Description",null=True)
    eventtype = models.ForeignKey(Eventtype, on_delete=models.CASCADE, verbose_name= "Event Type")
    eventlocation = models.ForeignKey(Eventlocation, on_delete=models.CASCADE, verbose_name= "Event Location")
    eventorganizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, verbose_name= "Event Orgainzer")
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    createdTime=models.DateTimeField(default=timezone.now)
    createdBy=models.ForeignKey(User,verbose_name= "created by", on_delete=models.CASCADE,default='2')
    active = models.BooleanField(default=1)

    # def save(self, *args, **kwargs):
    #     if self.endTime < timezone.now():
    #         self.active = False
    #     super(Event, self).save(int(self.active))
