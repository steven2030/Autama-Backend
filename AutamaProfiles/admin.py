from django.contrib import admin
from .models import AutamaProfile
from django.urls import path
from django.http import HttpResponseRedirect
from Nucleus.bacon import Bacon
from AutamaProfiles.models import create_new_autama


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
        bacon = Bacon() # For generating personality
        amount = 2 # Amount of Autama profiles to create
        username = str(request.user) # Username of user who presses the mass produce button

        for i in range(amount):
            personality = bacon.generate_full_personality()
            create_new_autama(personality=personality, creator=username)

        self.message_user(request, "Mass-production completed.")
        return HttpResponseRedirect("../")
