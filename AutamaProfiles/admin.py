from django.contrib import admin
from .models import AutamaProfile, AutamaGeneral
from django.urls import path
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from Nucleus.bacon import Bacon
from AutamaProfiles.views import create_autama_profile
from .views import get_meta


# Register your models here.
@admin.register(AutamaProfile)
class AutamaProfileAdmin(admin.ModelAdmin):
    change_list_template = "AutamaProfiles/autama_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('massproduce/', self.massproduce),
        ]
        return my_urls + urls

    def massproduce(self, request):
        count = request.POST.get('count')
        count = int(count)
        ag = get_meta()

        if count < 9999 and ag.autamaInProcess == 0:
            ag.autamaInProcess = count
            ag.save()
            amount = count  # The amount of Autama profiles to create
            bacon = Bacon()  # For generating personality
            username = str(request.user)  # Username of user who presses the mass produce button

            for i in range(amount):
                personality = bacon.generate_full_personality()
                create_autama_profile(personality=personality, creator=username)
                ag.autamaInProcess -= 1
                ag.save()

            self.message_user(request, "Mass-production completed.")
            return JsonResponse({'prog': 'Created ' + str(amount)})

        # Handle error return
        if ag.autamaInProcess > 0:
            return JsonResponse({'error': "Already in progress"}, status=500)
        return JsonResponse({'error': "Invalid mass produce number attempted."}, status=500)


admin.site.register(AutamaGeneral)
