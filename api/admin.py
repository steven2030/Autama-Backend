from django.contrib import admin
from .models import User, AutamaProfile, Matches
from .models import Messages


# Register your models here
admin.site.register(Messages)
admin.site.register(User)
admin.site.register(AutamaProfile)
admin.site.register(Matches)
