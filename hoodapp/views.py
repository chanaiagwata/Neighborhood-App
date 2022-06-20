from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Business, Profile, Post, Neighborhood
from .forms import DetailsForm, addHoodForm

# Create your views here.

def index(request):
    '''
    Function that renders the landing page
    '''
    return render(request, 'index.html')

@login_required()
def profile(request):
    posts = Post.objects.all()
    current_user = request.user 
    
    if request.method=='POST':
        details_form = DetailsForm(request.POST, request.FILES)
        
        if details_form.is_valid():
            profile = details_form.save(commit=False)
            profile.user = current_user
            profile.save()
            
        return redirect('profile')
        
    else:
        details_form = DetailsForm
        
    return render(request,'profile.html', {'details_form':details_form})

@login_required()
def update_profile(request):
    current_user = request.user
    if request.method== 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
            profile = Profile.objects.filter(id=current_user.profile.id).first()
            profile.profile_pic.delete()
            profile.profile_pic=form.cleaned_data["profile_pic"]
            profile.save()
        return redirect('profile')
    else:
        form = DetailsForm()
    return render(request, 'update_profile.html', {"form":form})


def hoods(request):
    hoods = Neighborhood.objects.all()
    # current_user = request.user
    
    if request.method=="POST":
        form = addHoodForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            hood = form.save(commit=False)
            form.save()
        return redirect('hoodpage')
    else:
        form=addHoodForm()
   
    return render(request, 'hoods.html',{'form':form, 'hoods':hoods})






def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "businesses":searched_businesses})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})