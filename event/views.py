from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Eventtype, Eventlocation, Organizer
from .forms import (NeweventForm, 
                    EditEventForm , 
                    addEventTypeForm,
                    addOrganizerForm,
                    addLocationForm,
                    editEventTypeForm,
                    editOrganizerForm,
                    editLocationForm,)
from django.contrib import messages
# Create your views here.

def eventhome(request):
    # list all objects from event models
    qs = Event.objects.filter(active=True)
    # qs = Event.objects.all()
    return render(request, 'event/eventall.html',{'events':qs})
    
def newevent(request):
    
    if request.method == "POST":
        form = NeweventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event:eventhome')
    else:
        event = NeweventForm()
        return render(request, 'event/newevent.html', {'form':event})


def editEvent(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EditEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Updated successfully",
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("event:eventhome")

    else:
        form = EditEventForm(instance=event)

    return render(request, "event/event_edit.html", {'form': form, 'event': event})


def eventManager(request):
    qst = Eventtype.objects.all()
    qso = Organizer.objects.all()
    qsl = Eventlocation.objects.all()
    return render(request, "event/event_admin.html", {'eventtype': qst, 'orgaizers': qso, 'locations': qsl})


def addEventType(request):
    if request.method == "POST":
        form = addEventTypeForm(request.POST)
        if form.is_valid():
            #check the eventorganizer already exist
            type= form.cleaned_data['eventtype']
            if Eventtype.objects.filter(eventtype=type).exists():
                print('coming here')
                messages.error(request, 'Location already exists',
                            extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('event:eventmanager')
            else:
                event = form.save(commit=False)
                event.save()
                return redirect('event:eventmanager')
    else:
        event = addEventTypeForm()
        return render(request, 'event/eventtype_add.html', {'form':event})

def addOrganizer(request):
    if request.method == "POST":
        form = addOrganizerForm(request.POST)
        if form.is_valid():
            #check the eventorganizer already exist
            organizer= form.cleaned_data['eventorganizer']
            if Organizer.objects.filter(eventorganizer=organizer).exists():
                print('coming here')
                messages.error(request, 'Location already exists',
                            extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('event:eventmanager')
            else:
                event = form.save(commit=False)
                event.save()
                return redirect('event:eventmanager')
    else:
        event = addOrganizerForm()
        return render(request, 'event/organizer_add.html', {'form':event})

def addLocation(request):
    if request.method == "POST":
        form = addLocationForm(request.POST)  

        if form.is_valid():
            #check the location already exist
            location= form.cleaned_data['location']
            if Eventlocation.objects.filter(location=location).exists():
                print('coming here')
                messages.error(request, 'Location already exists',
                            extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('event:eventmanager')
            else:
                event = form.save(commit=False)
                event.save()
                return redirect('event:eventmanager')
    else:
        event = addLocationForm()
        return render(request, 'event/location_add.html', {'form':event})

def editEventType(request):
    pass

def editOrganizer(request):
    pass

def editLocation(request):
    pass

def deleteEventType(request):
    pass

def deleteOrganizer(request):
    pass

def deleteLocation(request):
    pass
