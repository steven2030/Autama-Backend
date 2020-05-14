from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.forms import ModelForm
from AutamaProfiles.models import AutamaProfile, AutamaGeneral
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
import json
from Nucleus.pancake import Pancake


class AutamaForm(ModelForm):
    class Meta:
        model = AutamaProfile
        fields = ['creator', 'picture', 'first', 'last', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 'interest6']  # interests did exist here.


class CustomAutamaView(View):
    def post(self, request):
        creator = str(request.user)
        origin = creator
        picture = get_picture_name()
        first = request.POST.get('firstname')
        last = request.POST.get('lastname')
        interest1 = request.POST.get('interest1')
        interest2 = request.POST.get('interest2')
        interest3 = request.POST.get('interest3')
        interest4 = request.POST.get('interest4')
        interest5 = request.POST.get('interest5')
        interest6 = request.POST.get('interest6')

        new_autama = AutamaProfile.objects.create(creator=creator, picture=picture, first=first, last=last,
                                                  pickle=origin,
                                                  interest1=interest1, interest2=interest2,
                                                  interest3=interest3, interest4=interest4,
                                                  interest5=interest5, interest6=interest6)
        new_autama.save()

        current_user = User.objects.get(pk=request.user.pk)
        current_user.my_Autama += 1
        current_user.save()

        return HttpResponseRedirect(reverse('MyClaims'))


@login_required
def register_autama(request):
    if request.method == 'POST':
        form = AutamaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')

    else:
        form = AutamaForm()

    return render(request, "AutamaProfiles/register.html", {'form': form})


def profile(request, pk, slug):
    a_profile = get_object_or_404(AutamaProfile, pk=pk)
    return render(request, 'AutamaProfiles/autama_profile.html', {'profile': a_profile})


def browse(request):
    profiles = AutamaProfile.objects.all()
    return render(request, 'AutamaProfiles/browse.html', {'profiles': profiles})


def claim(request):
    a = request.POST.get("autama_id")
    profile = AutamaProfile.objects.get(pk=a)
    #profile.nummatches += 1
    profile.save()
    data = {'creator': profile.creator,
            'match_num': profile.nummatches}
    return HttpResponse(content=json.dumps(data),content_type='json/application')


def testfunc(request):
    meta_autama = AutamaGeneral.objects.get(pk=1)
    return HttpResponse(meta_autama.currentCount)


# A function to create a new Autama profile. origin is the username of the user the Autama was based off
def create_autama_profile(personality: list, creator: str = "Happy Slackers", origin: str = "Happy Slackers"):
    pancake = Pancake()  # For handling name generating
    REQUIRED = 6  # The required amount of traits
    amount = len(personality)

    # Make sure personality has the required amount of traits
    if amount == REQUIRED:
        # Get meta data on Autama Images and generate path for current autama picture
        picture = get_picture_name()
        
        first = pancake.generate_first_name()
        last = pancake.generate_last_name()
        interest1 = personality[0]
        interest2 = personality[1]
        interest3 = personality[2]
        interest4 = personality[3]
        interest5 = personality[4]
        interest6 = personality[5]

        new_autama = AutamaProfile.objects.create(creator=creator, picture=picture, first=first, last=last,
                                                     pickle=origin,
                                                     interest1=interest1, interest2=interest2,
                                                     interest3=interest3, interest4=interest4,
                                                     interest5=interest5, interest6=interest6)
        new_autama.save()


# A function to get meta data on Autama Images by first checking if it exists and then creating one if it doesn't
def get_meta():
    if not AutamaGeneral.objects.exists():
        # If queryset is empty, create a new query
        gen = AutamaGeneral()
        gen.currentCount = 1
        gen.totalCount = 100
        gen.save()

    # Get and return meta data
    meta_autama = AutamaGeneral.objects.first()
    return meta_autama


# A function to get a file name for a picture
def get_picture_name():
    meta_autama = get_meta()
    file_name = "a" + str(meta_autama.currentCount) + ".png"
    meta_autama.currentCount += 1
    meta_autama.save()
    return file_name
