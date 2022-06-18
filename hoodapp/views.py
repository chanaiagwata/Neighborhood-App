from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Business, Profile, Post, Neighborhood

# Create your views here.
def index(request):
    '''
    Function that renders the landing page
    '''
    return render(request, 'index.html')

def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "businesses":searched_businesses})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})