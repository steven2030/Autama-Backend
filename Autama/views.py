from django.http import HttpResponse
from accounts.models import User
from AutamaProfiles.models import AutamaProfile
import simplejson
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

import json
from django.shortcuts import render,reverse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from accounts.models import User, Messages, Matches
from django import forms
from django.db.models import Q
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from AutamaProfiles.models import AutamaProfile
from django.utils import timezone



class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = User.objects.get(Q(username=username) | Q(email=username))
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
    # TODO: Add additional profile features to register page
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

        user = User.objects.filter(Q(username=username) | Q(email=email))
        if user:
            return render(request, 'register.html', {'error': 'email or account already existed'})

        obj = User.objects.create(username=username, first_name=firstname,last_name=lastname, email=email)
        obj.set_password(password)
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
                obj = User.objects.get(id=int(user_id))
            except Exception as e:
                return render(request, 'error.html', {"error": "user does not exist"})
            if obj.id == int(user_id):
                return render(request, 'profile.html', {"user": obj, 'myself': True})
            return render(request, 'profile.html', {"user": obj, 'myself': False})

    def post(self, request):
        user_id = request.POST.get("id")
        last_name = request.POST.get("name")
        sex = request.POST.get("sex")
        email = request.POST.get("email")
        obj = User.objects.get(id=int(user_id))
        obj.last_name = last_name
        obj.sex = int(sex)
        obj.email = email
        obj.save()
        return HttpResponseRedirect(reverse("profile") + "?id=" + user_id)


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


# Webpage should be of the type:
# /FindMatches/?AID=#
class FindMatches(LoginRequiredMixin, View):
    # def get(self, request):
    #     a_id = request.GET['AID']
    #     autama =  AutamaProfile.objects.get(pk=a_id)
    #     data = {
    #         'autama_id': autama.id,
    #         'creator': autama.creator,
    #         'picture': autama.picture,
    #         'first': autama.first,
    #         'last': autama.last,
    #         'matches': autama.nummatches,
    #         'owner': autama.owner,
    #         'interest1': autama.interest1,
    #         'interest2': autama.interest2,
    #         'interest3': autama.interest3,
    #     }
    #     return JsonResponse(data)
    def get(self, request):
        return render(request, 'find_matches.html')


# TODO: Do we want this as part of login? Fix to view if keeping.
def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')


class MyMatches(LoginRequiredMixin, View):

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        user_matches = Matches.objects.all().filter(userID=user.pk).order_by('timeStamp')
        context = {'user_matches': user_matches}
        return render(request, 'my_matches.html', context)


def chat_main_page(request):
    return HttpResponse('Chat main page')


class MessageForm(forms.Form):
    x = forms.CharField(label='some text')


# TODO: make sure a user can only chat with an autama they have matched with.
# TODO: make sure autama id exists.
# TODO: validate all user input.
class Chat(LoginRequiredMixin, View):

    def get(self, request, pk):
        user = User.objects.get(pk=request.user.id)
        autama = AutamaProfile.objects.get(pk=pk)
        form = MessageForm()

        # Search for a message chain in the database order by utc timestamp
        message_chain = Messages.objects.all().filter(userID=user.pk).filter(autamaID=autama.pk).order_by('timeStamp')

        return render(request, 'Chat.html', {'autama': autama, 'user': user, 'form': form,
                                             'message_chain': message_chain})

    def post(self, request, pk):
        user = User.objects.get(pk=request.user.id)
        autama = AutamaProfile.objects.get(pk=pk)  # Check the validity of Autama id.
        form = MessageForm(request.POST)
        autama_response = "This is a response."

        a_message = Messages.objects.create(userID=user, autamaID=autama, sender=Messages.SENDER_CHOICES[0],
                                            message=form['x'].value())
        a_message.save()

        a_message = Messages.objects.create(userID=user, autamaID=autama, sender=Messages.SENDER_CHOICES[1],
                                            message=autama_response)
        a_message.save()

        return redirect('Chat', pk=pk)


