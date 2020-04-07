from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from AutamaProfiles.models import AutamaProfile
from django.contrib.auth.decorators import login_required


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

