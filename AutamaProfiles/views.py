from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.forms import ModelForm
from AutamaProfiles.models import AutamaProfile, AutamaGeneral
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import json
from Nucleus.pancake import Pancake
from Nucleus.bacon import Bacon


class AutamaForm(ModelForm):
    class Meta:
        model = AutamaProfile
        fields = ['creator', 'picture', 'first', 'last', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 'interest6']  # interests did exist here.


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


# A function to create a new Autama profile. origin is the username of the user the Autama was based off
def create_autama_profile(personality: list, creator: str = "Happy Slackers", origin: str = "Happy Slackers"):
    pancake = Pancake()  # For handling name generating
    first = pancake.generate_first_name()
    last = pancake.generate_last_name()
    create_custom_autama(creator, first, last, origin, personality)


# A function to create custom Autama
def create_custom_autama(creator: str, first: str, last: str, origin: str, personality: list):
    REQUIRED = 6  # The required amount of traits
    bacon = Bacon()
    # Make sure personality does not have "my name is" traits
    checked_personality = bacon.check_personality(personality)
    amount = len(checked_personality)

    # Make sure personality has the required amount of traits
    if amount == REQUIRED:
        # Get meta data on Autama Images and generate path for current autama picture
        picture = get_picture_name()

        interest1 = add_period(checked_personality[0])
        interest2 = add_period(checked_personality[1])
        interest3 = add_period(checked_personality[2])
        interest4 = add_period(checked_personality[3])
        interest5 = add_period(checked_personality[4])
        interest6 = add_period(checked_personality[5])

        new_autama = AutamaProfile.objects.create(creator=creator, picture=picture, first=first, last=last,
                                                  pickle=origin,
                                                  interest1=interest1, interest2=interest2,
                                                  interest3=interest3, interest4=interest4,
                                                  interest5=interest5, interest6=interest6)
        new_autama.save()


# A function to check if an interest ends  with a punctuation mark. If it does not, it will add a period.
# Also capitalizes first letter
def add_period(interest: str):
    i = interest.rstrip()
    i = i.lstrip()
    i = i.capitalize()

    period = i.endswith(".")
    question_mark = i.endswith("?")
    exclamation_point = i.endswith("!")

    # Add period if interest does not end with a punctuation mark
    if not period and not question_mark and not exclamation_point:
        revised_interest = i + "."
        return revised_interest
    else:
        return i


# A function to get meta data on Autama Images by first checking if it exists and then creating one if it doesn't
def get_meta():
    if not AutamaGeneral.objects.exists():
        # If queryset is empty, create a new query
        gen = AutamaGeneral()
        gen.currentCount = 1
        gen.totalCount = 100
        gen.autamaLimit = 10
        gen.autamaInProcess = 0
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


# A function to get the value of the maximum amount of Autamas an user can create
def get_my_autama_limit():
    meta_autama = get_meta()
    limit = meta_autama.autamaLimit
    return limit


@login_required()
def autama_in_progress(request):
    if request.method == 'GET':
        ag = get_meta()
        return JsonResponse({'inprogress': ag.autamaInProcess})
    if request.method == 'POST':
        return JsonResponse({'post': 'testing'})
