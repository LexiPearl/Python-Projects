from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    current_time= datetime.datetime.now()
    # i=date.datetime.now()
    # current_time= ("%s%s%s" % (i.day,i.month,i.year)) + ("%s:%s:%s" % (i.hour,i.month, i.second))
    context = {
        "current_time" : current_time
    }
    print datetime.datetime.now()
    return render(request,'timedisplay/index.html', context)
