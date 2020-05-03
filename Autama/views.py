from django.http import HttpResponse
from accounts.models import User
from AutamaProfiles.models import AutamaProfile
import simplejson
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

import json
from django.shortcuts import render, reverse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from accounts.models import User, Messages, Matches, Claims
from django import forms
from django.db import IntegrityError
from django.db.models import Q
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from AutamaProfiles.models import AutamaProfile
from django.utils import timezone
from Nucleus.ham import Ham


def claim_autama(user_pk, autama_pk):
    autama = AutamaProfile.objects.get(pk=autama_pk)  # Validation needed here
    user = User.objects.get(pk=user_pk)
    ret = True

    if Claims.objects.filter(autamaID=autama).exists():
        ret = False

    else:
        # you can claim this, so claim it
        new_claim = Claims(autamaID=autama, userID=user)
        new_claim.save()

    return ret


def unclaim_autama(user_pk, autama_pk):
    autama = AutamaProfile.objects.get(pk=autama_pk)  # Validation needed here
    user = User.objects.get(pk=user_pk)
    ret = True

    if Claims.objects.filter(userID=user).filter(autamaID=autama).exists():
        # remove claim
        Claims.objects.filter(autamaID=autama).delete()

    else:
        # there is nothing to unclaim.
        ret = False

    return ret


def match(user_pk, autama_pk):
    autama = AutamaProfile.objects.get(pk=autama_pk)
    user = User.objects.get(pk=user_pk)
    ret = True

    if Matches.objects.filter(userID=user).filter(autamaID=autama).exists():
        ret = False

    else:
        new_match = Matches(userID=user, autamaID=autama)
        new_match.save()

    return ret


def unmatch(user_pk, autama_pk):
    user = User.objects.get(pk=user_pk)
    autama = AutamaProfile.objects.get(pk=autama_pk)
    ret = True

    if Matches.objects.filter(userID=user).filter(autamaID=autama).exists():
        # unmatch
        Matches.objects.filter(userID=user).filter(autamaID=autama).delete()

    else:
        ret = False

    return ret


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

        obj = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email)
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
        return HttpResponse(json.dumps({'code': 0, "avatar": obj.image.url}))


class ResetPasswordView(LoginRequiredMixin, View):
    def post(self, request):
        obj = User.objects.get(id=request.user.id)
        password = request.POST.get("password")
        obj.set_password(password)
        obj.save()
        return HttpResponse(json.dumps({'code': 0, "avatar": obj.image.url}), content_type="application/json")


# Webpage should be of the type:
# /FindMatches/?AID=#
class FindMatches(LoginRequiredMixin, View):
    def get(self, request):
        a_id = request.GET.get('AID')

        # Returns the base HTML.
        if a_id is None:
            user = User.objects.get(id=request.user.id)
            return render(request, 'find_matches.html', {'autama_id': user.currentAutama})

        # Returns JSON with Autama Profile data
        autama = AutamaProfile.objects.get(pk=a_id)
        data = {
            'autama_id': autama.id,
            'creator': autama.creator,
            'first': autama.first,
            'last': autama.last,
            'matches': autama.nummatches,
            'owner': autama.owner,
            'interest1': autama.interest1,
            'interest2': autama.interest2,
            'interest3': autama.interest3,
        }
        return JsonResponse(data)

    def post(self, request):
        data = request.POST.copy()
        ret = False

        AID = data.get('AID')
        if data.get('match') == '1':
            ret = match(request.user.id, AID)
        user = User.objects.get(pk=request.user.id)
        user.currentAutama += 1
        user.save()
        if ret:
            return HttpResponse(status=200)
        else:
            return JsonResponse({"user": request.user.id, "Autama": AID})


# TODO: Do we want this as part of login? Fix to view if keeping.
def about(request):
    return render(request, 'about.html')


def PrivacyPolicy(request):
    return render(request, 'privacy_policy.html')


def unclaim_from_chat(request, pk):
    unclaim_autama(request.user.id, pk)
    return redirect('Chat', pk=pk)


class MyClaims(LoginRequiredMixin, View):

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        claims = Claims.objects.filter(userID=user).order_by('timeStamp')
        context = {'claims': claims}
        return render(request, 'my_claims.html', context)

    def post(self, request, pk):
        unclaim_autama(request.user.id, pk)
        return redirect('MyClaims')
        # return HttpResponse('Hello!')


class MyMatches(LoginRequiredMixin, View):

    def get_matches(self, user, query_string=None):
        have_chatted = Messages.objects.filter(userID=user).values_list('autamaID', flat=True)
        not_chatted = Matches.objects.filter(userID=user.pk).exclude(autamaID__in=have_chatted)
        user_matches = not_chatted

        if query_string:
            user_matches = [a_match for a_match in not_chatted if
                            query_string in a_match.autamaID.first + " " + a_match.autamaID.last]

        return user_matches

    def get_messages(self, user, query_string=None):
        # get ids of all autama user messaged
        autama_id_list = Messages.objects.all().filter(userID=user.pk).order_by('timeStamp') \
            .values_list('autamaID', flat=True)

        if query_string:
            autama_id_list = [an_id.autamaID.pk for an_id in autama_id_list if
                              query_string in an_id.message or
                              query_string in an_id.autamaID.first + " " + an_id.autamaID.last]

        autama_id_list = list(set(autama_id_list))
        user_messages = AutamaProfile.objects.all().filter(id__in=autama_id_list)
        messages = [Messages.objects.all().filter(userID=user).filter(autamaID=an_id).order_by('timeStamp')
                        .reverse()[0].message for an_id in autama_id_list]

        message_chain = [" ".join([a_message.message for a_message in Messages.objects.all()
                                  .filter(userID=user.pk)
                                  .filter(autamaID=aid)
                                  .order_by('timeStamp')])
                         for aid in autama_id_list]

        return list(zip(user_messages, messages, message_chain))  # (ProfileList, a single last message)

    def get(self, request):
        user = User.objects.get(pk=request.user.id)  # get user
        user_matches = self.get_matches(user=user)  # get all user matches
        user_messages = self.get_messages(user=user)
        context = {'user_matches': user_matches, 'num_matches': len(user_matches),
                   'user_messages': user_messages, 'num_messages': len(user_messages)}

        return render(request, 'my_matches.html', context)

    def post(self, request):
        query_string = request.POST.get('search_bar')
        user = User.objects.get(pk=request.user.id)
        user_matches = self.get_matches(user=user, query_string=query_string)
        user_messages = self.get_messages(user=user, query_string=query_string)
        context = {'user_matches': user_matches, 'num_matches': len(user_matches),
                   'user_messages': user_messages, 'num_messages': len(user_messages)}

        return render(request, 'my_matches.html', context)


def chat_main_page(request):
    return HttpResponse('Chat main page')


class MessageForm(forms.Form):
    x = forms.CharField(widget=forms.Textarea(attrs={'class': 'special'}), label="")


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

        return render(request, 'chat.html', {'autama': autama, 'user': user, 'form': form,
                                             'message_chain': message_chain})

    def post(self, request, pk):
        user = User.objects.get(pk=request.user.id)
        autama = AutamaProfile.objects.get(pk=pk)  # Check the validity of Autama id.
        form = MessageForm(request.POST)

        a_message = Messages.objects.create(userID=user, autamaID=autama, sender=Messages.SENDER_CHOICES[0][1],
                                            message=form['x'].value())
        a_message.save()

        # The test_name and test_personality are just for testing. They will be replaced.
        first_name = "Happy Slackers"
        last_name = "Autama"
        trait1 = autama.interest1
        trait2 = autama.interest2
        trait3 = autama.interest3
        trait4 = autama.interest4
        trait5 = autama.interest5
        trait6 = autama.interest6
        personality = [trait1, trait2, trait3, trait4, trait5, trait6]

        ham = Ham(first_name, last_name, personality)
        autama_response = ham.converse(user_input=form['x'].value())

        a_message = Messages.objects.create(userID=user, autamaID=autama, sender=Messages.SENDER_CHOICES[1][1],
                                            message=autama_response)
        a_message.save()

        return redirect('Chat', pk=pk)


def testdata(request):
    if request.user.is_superuser or request.user.is_staff:
        try:
            from Autama.testdata import add_test_data
            add_test_data()
            return HttpResponse("Test Data Added")
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return HttpResponse("Already Added")
