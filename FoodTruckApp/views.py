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


def index(request):
    context = {}
    return render(request,'FoodTruckApp/base.html', context)

def menu(request):
    context = {}
    return render(request,'FoodTruckApp/menu.html', context)
