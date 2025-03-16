from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout




# Create your views here.


def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('trainee_list')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'user/login.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trainee_list')

    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {'form': form})





def logout_view(request):
    logout(request)
    return redirect('login')