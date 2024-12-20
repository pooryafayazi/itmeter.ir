from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')



    if not request.user.is_authenticated:      

        return render(request, 'accounts/login.html')


#def logout_view(request):
    #return render(request, 'accounts/logout.html')


def signup_view(request):
    return render(request, 'accounts/signup.html')