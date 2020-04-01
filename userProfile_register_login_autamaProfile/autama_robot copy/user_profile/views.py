import json
from django.shortcuts import render,reverse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from user_profile.models import UserProfile, RobotModel
from django.db.models import Q
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginRequiredMixin(object):
    """

    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/login/')


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')
        if password != rePassword:
            return render(request, 'register.html', {'error': 'Inconsistent passwords'})
        interest = []
        interest.append(request.POST.get('interest1', ''))
        interest.append(request.POST.get('interest2', ''))
        interest.append(request.POST.get('interest3', ''))
        interest.append(request.POST.get('interest4', ''))
        interest.append(request.POST.get('interest5', ''))
        interest.append(request.POST.get('interest6', ''))
        user = UserProfile.objects.filter(Q(username=username) | Q(email=email))
        if user:
            return render(request, 'register.html', {'error': 'email or account already existed'})

        obj = UserProfile.objects.create(username=username, first_name=firstname, last_name=lastname, email=email)
        obj.set_password(password)
        obj.interest = ';'.join(interest)
        obj.save()
        return HttpResponseRedirect(reverse('login'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

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
                return render(request, "login.html", {"error": "The user is not activated!"})
        else:
            return render(request, "login.html", {"error": "username or account is incorrect！"})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_id = request.GET.get("user_id")
        if not user_id:
            return render(request, 'profile.html', {"user": request.user, 'myself': True})
        else:
            try:
                obj = UserProfile.objects.get(id=int(user_id))
            except Exception as e:
                return render(request, 'error.html', {"error": "user does not exist"})
            if obj.id == int(user_id):
                return render(request, 'profile.html', {"user": obj, 'myself': True})
            return render(request, 'profile.html', {"user": obj, 'myself': False})

    def post(self, request):
        user_id = request.POST.get("id")
        last_name = request.POST.get("name")
        interest = request.POST.get("interest")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        obj = UserProfile.objects.get(id=int(user_id))
        obj.last_name = last_name
        obj.interest = interest
        obj.sex = int(sex)
        obj.address = address
        obj.phone = phone
        obj.email = email
        obj.save()
        return HttpResponseRedirect(reverse("profile") + "?id=" + user_id)



class ChangeAvatarView(LoginRequiredMixin, View):

    def post(self, request):
        obj = UserProfile.objects.get(id=request.user.id)
        pic = ContentFile(request.FILES['file'].read())
        obj.image.save(request.FILES['file'].name, pic)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}))


class ResetPasswordView(LoginRequiredMixin, View):
    def post(self, request):
        obj = UserProfile.objects.get(id=request.user.id)
        password = request.POST.get("password")
        obj.set_password(password)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}), content_type="application/json")


class RobotView(LoginRequiredMixin, View):
    def get(self, request):
        robot_id = request.POST.get("robot_id")
        if robot_id:
            robot = RobotModel.objects.get(id=int(robot_id))
        else:
            robot = RobotModel.objects.all()[0]
        return render(request, 'robot.html', {"robot": robot})

    def post(self, request):
        robot_id = request.POST.get("robot_id")
        obj = RobotModel.objects.get(id=int(robot_id))
        obj.match_number += 1
        obj.creator = request.user.username
        obj.save()
        return HttpResponse(json.dumps({'code':0, "creator": obj.creator, "match_number": obj.match_number}), content_type="application/json")


