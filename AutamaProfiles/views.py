from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from AutamaProfiles.models import AutamaProfile

# Create your views here.
class AutamaForm(ModelForm):
    class Meta:
        model = AutamaProfile
        fields = ['creator', 'picture', 'first', 'last', 'pickle', 'interests']


# HttpRequest.content_params
def register_autama(request):
    if request.method == 'POST':
        form = AutamaForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to another page
            return redirect('Autama:homepage')

    else:
        form = AutamaForm()

    return render(request, "AutamaProfiles/register.html", {'form': form})
