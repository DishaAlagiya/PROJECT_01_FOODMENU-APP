from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {user}, you have been successfully logged in')
            print(f'messages:{messages} ')

            return redirect('login')
        else: 
            print(f'There is error in form validation: {form.errors}')
            return render(request, 'users/register.html', {'form': form})
        
    form= RegisterForm()
    context={
        'form':form
    }
    return render(request,'users/register.html',context)

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

