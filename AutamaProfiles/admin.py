from django.contrib import admin
from .models import AutamaProfile
from django.urls import path
from django.http import HttpResponseRedirect
from Nucleus.bacon import Bacon
from Nucleus.pancake import Pancake

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
        REQUIRED = 6 # Required number of traits
        bacon = Bacon() # For generating personality
        pancake = Pancake() # For generating name
        amount = 2 # Amount of Autama profiles to create

        for i in range(amount):
            personality = bacon.generate_full_personality()
            trait_amount = len(personality)

            # Make sure personality has the required amount of traits
            if trait_amount == REQUIRED:
                creator = "Happy Slackers"
                picture = "Images/a0.png"
                first = pancake.generate_male_name()
                last = "last name"
                interest1 = personality[0]
                interest2 = personality[1]
                interest3 = personality[2]
                interest4 = personality[3]
                interest5 = personality[4]
                interest6 = personality[5]

                hybrid_autama = AutamaProfile.objects.create(creator=creator, picture=picture, first=first, last=last,
                                                             interest1=interest1, interest2=interest2,
                                                             interest3=interest3, interest4=interest4,
                                                             interest5=interest5, interest6=interest6)
                hybrid_autama.save()

        self.message_user(request, "Mass-production completed.")
        return HttpResponseRedirect("../")
