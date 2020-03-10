from django.http import HttpResponse
from accounts.models import UserProfile
import simplejson
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')


@login_required
def chat(request):
    return render(request, 'chat.html')


@login_required
def find_matches(request):
    return render(request, 'find_matches.html')


@login_required
def my_matches(request):
    return render(request, 'my_matches.html')

@login_required
def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')


def pagelogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')


@login_required
def test_db_lookup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        try:
            db_Out = UserProfile.objects.get(username=uname)
        except UserProfile.DoesNotExist:
            return HttpResponse(simplejson.dumps({"uname":"Does not exist"}), content_type='application/json')
            #return HttpResponse("Profile does not exist")
        response_dict = {
            'uname': db_Out.username,
            'email': db_Out.email,
            'first': db_Out.first,
            'last': db_Out.last,
            'int1': db_Out.interests1,
            'int2': db_Out.interests2,
            'int3': db_Out.interests3,
            'int4': db_Out.interests4,
            'int5': db_Out.interests5
        }

        return render(request, 'test_db_lookup.html', response_dict)
        #return HttpResponse(simplejson.dumps(response_dict),
        #                   content_type='application/json')
    return render(request, 'test_db_lookup.html')


@login_required
def test_db_add(request):
    if request.method == "POST":
        entry = UserProfile()
        entry.username = request.POST.get('uname')
        entry.email = request.POST.get('email')
        entry.first = request.POST.get('fname')
        entry.last = request.POST.get('lname')
        entry.picture = '/Images/User' + str(entry.username)
        entry.interests1 = request.POST.get('int1')
        entry.interests2 = request.POST.get('int2')
        entry.interests3 = request.POST.get('int3')
        entry.interests4 = request.POST.get('int4')
        entry.interests5 = request.POST.get('int5')
        entry.save()

        return HttpResponse('Successfully Added')
    else:
        return render(request, 'test_db_add.html')
