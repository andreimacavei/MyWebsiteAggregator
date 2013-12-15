# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

dummyFeeds = [
    {
        'title': 'First Article',
        'description': 'Some desc',
        'link': '#',
        'pubdate': '15/12/2013'
    },
    {
        'title': 'Second Article',
        'description': 'Other desc',
        'link': '#',
        'pubdate': '14/12/2013'
    }
]

dummySubscriptions = [
    {
        'name': '1st website',
        'url': '#'
    },
    {
        'name': '2nd website',
        'url': '#'
    }
]

def homepage(request):
    return render(request, 'index.html', {
        'feeds': dummyFeeds,
        'subscriptions': dummySubscriptions
    })
