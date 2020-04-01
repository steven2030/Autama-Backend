from django.contrib import admin
from .models import *
# Register your models here.


class UserProfileAdmin(admin.AdminSite):
    list_display = ('username', 'email', 'mobile', 'is_superuser', 'date_joined', 'interest')
    search_fields = ('username', 'email', 'phone',)
    list_filter = ('date_joined',)

admin.site.register(UserProfile)



class RobotModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'fname', 'lname', 'owner', 'year',
                    'interest', 'match_number', 'creator')
    list_per_page = 20

admin.site.register(RobotModel, RobotModelAdmin)