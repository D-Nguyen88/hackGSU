from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            initial_group = Group.objects.get(name = 'lvl2')
            initial_group.user_set.add(user)
            login(request, user)
            return redirect('/WorkPlan/dashboard.html')
    else:
        form = UserCreationForm()
    context =  {
        'form':form
    }
    return render(request, 'registration/register.html', context)

<<<<<<< HEAD
def view_user_profile(request):
    get_user_obj = UserProfile.objects.get(username=request.user)
    return render(request, url, context)

def view_truck_profile(request):
    get_user_obj = Truck.objects.get(username=request.user)
    return render(request, url, context)

def view_announcements(request):
    get_announcements_obj = Announcements.objects.filter(pk=Truck)
    return render(request, url, context)

    
=======

def index(request):
    context = {}
    return render(request,'FoodTruckApp/base.html', context)
>>>>>>> 42a02671455861bf1bd5a64b482a34cca773dbbc
