from django.shortcuts import render
# Create your views here.

def index(request):
    meetups = [
        { 
            'title': 'A First Meetup', 
            'location': 'New York', 
            'slug': 'a-first-meetup' },
        { 
            'title': 'second', 
            'location': 'Paris', 
            'slug': 'a-second-meetup' }
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups' : True,
        'meetups': meetups
    })