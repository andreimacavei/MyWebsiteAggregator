# Create your views here.
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Webdev RSS Reader Wannabe")