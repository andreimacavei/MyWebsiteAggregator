from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime

def home(request):
    return HttpResponse("Hello again World!")

def current_date(request):
    now = datetime.datetime.now()
    return render(request, 'date/current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'date/hours_ahead.html',
        {'hour_offset': offset, 'next_time': dt})