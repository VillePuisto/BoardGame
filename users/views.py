from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

#Register a new user
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # 1 blanky boi
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():            
            new_user = form.save()
            #Log the user into the site and onto the home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('boardgames:index'))

    context = {'form': form}
    return render(request, 'registration/register.html', context)