from django.contrib import admin
from .models import AutamaInfo, UserInfo
from .models import Matches, Messages


# Import and Register your models here
admin.site.register(AutamaInfo)
admin.site.register(UserInfo)
admin.site.register(Matches)
admin.site.register(Messages)

