from django.contrib import admin
from .models import AutamaProfile
from django.urls import path
from django.http import HttpResponseRedirect

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
        self.message_user(request, "Mass-production complete.")
        return HttpResponseRedirect("../")
