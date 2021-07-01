from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    #view function that renders the home page
    return render(request, 'welcome.html')

