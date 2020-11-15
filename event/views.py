from django.shortcuts import render, redirect
from .models import Event
from .forms import NeweventForm
# Create your views here.

def eventhome(request):
    # list all objects from event models
    qs = Event.objects.all()
    return render(request, 'event/eventall.html',{'events':qs})
    
def newevent(request):
    
    if request.method == "POST":
        form = NeweventForm(request.POST)
        if form.is_valid():
            ename = form.cleaned_data['eventname']
            edescription = form.cleaned_data['eventdescription']
            etype = form.cleaned_data['eventtype']
            elocation = form.cleaned_data['eventlocation']
            eorganizer = form.cleaned_data['eventorganizer']
            stime = form.cleaned_data['starttime']
            etime = form.cleaned_data['endtime']
            event = Event(eventname=ename, eventdescription= edescription, eventtype=etype, eventlocation=elocation,
            eventorganizer=eorganizer,starttime=stime,endtime=etime)
            event.save()
            return redirect('eventhome')
    else:
        event = NeweventForm()
        return render(request, 'event/newevent.html', {'form':event})