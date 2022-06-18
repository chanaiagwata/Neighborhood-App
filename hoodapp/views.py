from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    '''
    Function that renders the landing page
    '''
    return render(request, 'index.html')