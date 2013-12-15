# Create your views here.
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

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

def get_feeds(request):
    # Check if user is authenticated first
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

@csrf_exempt
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
