from django.contrib import admin
from .models import Autama, User
from .models import Matches, Messages


# Register your models here
admin.site.register(Autama)
admin.site.register(User)
admin.site.register(Matches)
admin.site.register(Messages)

