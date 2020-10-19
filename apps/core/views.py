from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def homepage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    args = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request,user)
            return redirect('homepage')
        else:
            print(form.errors)
        
    else:
        form = UserCreationForm()
    
    return render(request, 'core/signup.html', {'form': form })