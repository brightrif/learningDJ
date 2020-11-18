from django import forms
from .models import Event, Eventtype, Eventlocation,Organizer

class NeweventForm(forms.ModelForm):
    eventname = forms.CharField(label='Event Name', max_length=200)
    eventdescription = forms.CharField(label='Description', max_length=300)
    eventtype = forms.ModelChoiceField(label='Event Type', queryset=Eventtype.objects.all())
    eventlocation = forms.ModelChoiceField(label='Location', queryset=Eventlocation.objects.all())
    eventorganizer = forms.ModelChoiceField(label='Orgainzed By', queryset=Organizer.objects.all())
    startTime = forms.DateTimeField(label='Start Time')
    endTime = forms.DateTimeField(label='End Time')

    class Meta:
        model = Event
        fields = ['eventname', 'eventdescription', 'eventtype', 'eventlocation','eventorganizer','startTime','endTime']
        # widgets = {
        #     'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        # }

# widget=forms.TextInput(attrs={'class': 'control-label'})
#  widget=forms.TextInput(attrs={'class': 'control-label'})
#  ,widget=forms.Select(attrs={'class': 'control-label'})

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['eventname', 'eventdescription', 'eventtype', 'eventlocation','eventorganizer','startTime','endTime' ]
        # widgets = {
        #     'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        # }


class addEventTypeForm(forms.ModelForm):
    class Meta:
        model = Eventtype
        fields = ['eventtype', ]

class addOrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['eventorganizer', ]
class addLocationForm(forms.ModelForm):
    class Meta:
        model = Eventlocation
        fields = ['location', ]

class editEventTypeForm(forms.ModelForm):
    class Meta:
        model = Eventtype
        fields = ['eventtype', ]

class editOrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['eventorganizer', ]

class editLocationForm(forms.ModelForm):
    class Meta:
        model = Eventlocation
        fields = ['location', ]


