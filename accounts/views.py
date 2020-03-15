from django.shortcuts import render, redirect
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.views import View
import json
from django.shortcuts import render,reverse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from .models import User


class RegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, '../templates/register.html')
        else:
            # Might want to change to error instead
            return redirect('FindMatches')

    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')
        if password != rePassword:
            return render(request, '../templates/register.html', {'error': 'Inconsistent passwords'})

        user = User.objects.filter(Q(username=username) | Q(email=email))
        if user:
            return render(request, '../templates/register.html', {'error': 'email or account already existed'})

        obj = User.objects.create(username=username, first_name=firstname,last_name=lastname, email=email)
        obj.set_password(password)
        obj.save()
        return HttpResponseRedirect(reverse('login'))


class LoginRequiredMixin(object):
    """
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/login/')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_id = request.GET.get("user_id")
        if not user_id:
            return render(request, '../templates/profile.html', {"user": request.user, 'myself': True})
        else:
            try:
                obj = User.objects.get(id=int(user_id))
            except Exception as e:
                return render(request, 'error.html', {"error": "user does not exist"})
            if obj.id == int(user_id):
                return render(request, '../templates/profile.html', {"user": obj, 'myself': True})
            return render(request, '../templates/profile.html', {"user": obj, 'myself': False})

    def post(self, request):
        user_id = request.POST.get("id")
        last_name = request.POST.get("name")
        interest = request.POST.get("interest")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        obj = User.objects.get(id=int(user_id))
        obj.last_name = last_name
        obj.interest = interest
        obj.sex = int(sex)
        obj.address = address
        obj.phone = phone
        obj.email = email
        obj.save()
        return HttpResponseRedirect(reverse("profile") + "?id=" + user_id)


class LoginView(View):
    def get(self, request):
        return render(request, '../templates/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_remember_me = request.POST.get('is_remember_me')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session.set_expiry(0)
                if is_remember_me:
                    request.session.set_expiry(None)
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, "../templates/login.html", {"error": "The user is not activated!"})
        else:
            return render(request, "..templates/login.html", {"error": "username or account is incorrect！"})


@login_required()
def profile(request):
    return render(request, 'accounts/templates/profile.html')

@login_required()
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)