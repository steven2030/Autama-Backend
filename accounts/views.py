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
from AutamaProfiles.models import AutamaProfile
from Nucleus.bacon import Bacon
from Nucleus.pancake import Pancake


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
        interests1 = request.POST.get('interest1')
        interests2 = request.POST.get('interest2')
        interests3 = request.POST.get('interest3')
        interests4 = request.POST.get('interest4')
        interests5 = request.POST.get('interest5')
        interests6 = request.POST.get('interest6')

        if password != rePassword:
            return render(request, '../templates/register.html', {'error': 'Inconsistent passwords'})

        user = User.objects.filter(Q(username=username) | Q(email=email))
        if user:
            return render(request, '../templates/register.html', {'error': 'email or account already existed'})

        obj = User.objects.create(username=username, first_name=firstname,last_name=lastname, email=email)
        obj.set_password(password)
        obj.interests1 = interests1
        obj.interests2 = interests2
        obj.interests3 = interests3
        obj.interests4 = interests4
        obj.interests5 = interests5
        obj.interests6 = interests6
        obj.save()

        # Creating a hybrid freak Autama
        bacon = Bacon()
        pancake = Pancake()
        user_personality = [interests1, interests2, interests3, interests4, interests5, interests6]
        hybrid_personality = bacon.make_hybrid_freak(user_personality)

        creator = "Happy Slackers"
        picture = "Images/a0.png"
        first = pancake.generate_male_name()
        last = "last name"
        interest1 = hybrid_personality[0]
        interest2 = hybrid_personality[1]
        interest3 = hybrid_personality[2]
        interest4 = hybrid_personality[3]
        interest5 = hybrid_personality[4]
        interest6 = hybrid_personality[5]

        hybrid_autama = AutamaProfile.objects.create(creator=creator, picture=picture, first=first, last=last, interest1=interest1, interest2=interest2, interest3=interest3, interest4=interest4, interest5=interest5, interest6=interest6)
        hybrid_autama.save()

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
                return render(request, '../templates/error.html', {"error": "user does not exist"})
            if obj.id == int(user_id):
                return render(request, '../templates/profile.html', {"user": obj, 'myself': True})
            return render(request, '../templates/profile.html', {"user": obj, 'myself': False})

    def post(self, request):
        user_id = request.POST.get("id")
        user_name = request.POST.get("name")
        interest = request.POST.get("interest")
        sex = request.POST.get("sex")
        email = request.POST.get("email")
        obj = User.objects.get(id=int(user_id))
        obj.username = user_name
        obj.interest = interest
        obj.sex = int(sex)
        obj.email = email
        obj.save()
        return HttpResponseRedirect(reverse("accounts:profile"))


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
                return HttpResponseRedirect(reverse("FindMatches"))
            else:
                return render(request, "../templates/login.html", {"error": "The user is not activated!"})
        else:
            return render(request, "..templates/login.html", {"error": "username or account is incorrect！"})


class ChangeAvatarView(LoginRequiredMixin, View):
    def post(self, request):
        obj = User.objects.get(id=request.user.id)
        pic = ContentFile(request.FILES['file'].read())
        obj.image.save(request.FILES['file'].name, pic)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}))


class ResetPasswordView(LoginRequiredMixin, View):
    def post(self, request):
        obj = User.objects.get(id=request.user.id)
        password = request.POST.get("password")
        obj.set_password(password)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}), content_type="application/json")


