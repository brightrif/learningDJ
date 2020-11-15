from django.db import models


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
    eventname = models.CharField(max_length=200)
    eventdescription = models.CharField(max_length=300)
    eventtype = models.ForeignKey(Eventtype, on_delete=models.CASCADE)
    eventlocation = models.ForeignKey(Eventlocation, on_delete=models.CASCADE)
    eventorganizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()


