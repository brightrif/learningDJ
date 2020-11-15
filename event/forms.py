from django import forms
from .models import Event, Eventtype, Eventlocation,Organizer

class NeweventForm(forms.Form):
    eventname = forms.CharField(max_length=200)
    eventdescription = forms.CharField(max_length=300)
    eventtype = forms.ModelChoiceField(queryset=Eventtype.objects.all())
    eventlocation = forms.ModelChoiceField(queryset=Eventlocation.objects.all())
    eventorganizer = forms.ModelChoiceField(queryset=Organizer.objects.all())
    starttime = forms.DateTimeField()
    endtime = forms.DateTimeField()



