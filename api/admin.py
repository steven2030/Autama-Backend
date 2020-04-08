from django.contrib import admin
from .models import AutamaProfile, User, Messages


admin.site.register(AutamaProfile)
admin.site.register(User)
admin.site.register(Messages)
