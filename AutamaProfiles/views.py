from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import ModelForm
from AutamaProfiles.models import AutamaProfile
from accounts.views import LoginRequiredMixin
from django.views import View
import json


# Create your views here.
class AutamaForm(ModelForm):
    class Meta:
        model = AutamaProfile
        fields = ['creator', 'picture', 'first', 'last', 'interests']


# HttpRequest.content_params
def register_autama(request):
    if request.method == 'POST':
        form = AutamaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
#            autama_instance = form.save(commit=False)
#            autama_instance.slug = str(autama_instance.pk) + autama_instance.first + autama_instance.last
            # redirect to another page
            return redirect('about')

    else:
        form = AutamaForm()

    return render(request, "AutamaProfiles/register.html", {'form': form})


def profile(request, pk, slug):
    a_profile = get_object_or_404(AutamaProfile, pk=pk)
    return HttpResponse(a_profile.get_slug())


def browse(request):
    profiles = AutamaProfile.objects.all()
    return render(request, 'AutamaProfiles/browse.html', {'profiles':profiles})


class RobotView(LoginRequiredMixin, View):
    def get(self, request):
        robot_id = request.POST.get("robot_id")
        if robot_id:
            robot = AutamaProfile.objects.get(id=int(robot_id))
        else:
            robot = AutamaProfile.objects.all()[0]
        return render(request, '../templates/robot.html', {"robot": robot})

    def post(self, request):
        robot_id = request.POST.get("robot_id")
        obj = AutamaProfile.objects.get(id=int(robot_id))
        obj.match_number += 1
        obj.creator = request.user.username
        obj.save()
        return HttpResponse(json.dumps({'code': 0, "creator": obj.creator, "match_number": obj.match_number}),
                            content_type="application/json")
