from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout # handle authentication (email)
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authentication via email, on hold for now
            # need to include authenticate backends if reimplementing
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            #log the user in
            return redirect('homepage')

    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'accounts/profile.html')