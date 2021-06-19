from django.shortcuts import render
# Create your views here.

def index(request):
    meetups = [
        { 'title': 'A First Meetup'},
        { 'title': 'second'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups' : True,
        'meetups': meetups
    })