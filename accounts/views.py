from django.shortcuts import render, redirect
import json
from django.shortcuts import render,reverse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from .models import User, Matches
from Nucleus.bacon import Bacon
from AutamaProfiles.views import create_autama_profile
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


# TODO: Need to implement email ping validation complete or remove stub.
class RegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, '../templates/register.html')
        else:
            # Might want to change to error instead
            return redirect('FindMatches')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')

        # Neither of the users names are being used for Autama generation.
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        interests1 = request.POST.get('interest1')
        interests2 = request.POST.get('interest2')
        interests3 = request.POST.get('interest3')
        interests4 = request.POST.get('interest4')
        interests5 = request.POST.get('interest5')
        interests6 = request.POST.get('interest6')

        if password != rePassword:
            return render(request, '../templates/register.html', {'error': 'Passowrds don\'t match.'})

        try:
            validate_email(email)
        except ValidationError:
            return render(request, '../templates/register.html', {'error': 'Invalid email address.'})

        if User.objects.filter(username=username) or User.objects.filter(email=email):
            return render(request, '../templates/register.html', {'error': 'Username or email already exists.'})

        obj = User.objects.create(username=username, email=email, currentAutama=1, nextAutama=2)
        obj.set_password(password)
        if interests1:
            obj.interests1 = interests1
            obj.interests2 = interests2
            obj.interests3 = interests3
            obj.interests4 = interests4
            obj.interests5 = interests5
            obj.interests6 = interests6

            bacon = Bacon()  # For handling personality generating
            # A list of the new user's interests
            user_personality = [interests1, interests2, interests3, interests4, interests5, interests6]
            # Creating an Autama with the same interests as the user
            same_personality = bacon.check_personality(user_personality)
            create_autama_profile(personality=same_personality, creator=username, origin=username)

        obj.save()
        
        # Login and redirect to find_matches
        login(request, obj)
        return HttpResponseRedirect("/")


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
        matches = Matches.objects.all().filter(userID=request.user.id).count()
        if not user_id:
            return render(request, '../templates/profile.html', {"user": request.user, 'myself': True, 'num_matches': matches})
        else:
            try:
                obj = User.objects.get(id=int(user_id))
            except Exception as e:
                return render(request, '../templates/error.html', {"error": "user does not exist"})
            if obj.id == int(user_id):
                return render(request, '../templates/profile.html', {"user": obj, 'myself': True, 'num_matches': matches})
            return render(request, '../templates/profile.html', {"user": obj, 'myself': False, 'num_matches': matches})

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


