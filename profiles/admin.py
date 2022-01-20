from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from profiles.models import Profile

# Register your models here.

@admin.register(Profile)
class userProfile(admin.ModelAdmin):
    list_display = ('user','position','Sdktype','picture')


class ProfileInline(admin.StackedInline):
    model = Profile

class ProfileAdmin (BaseUserAdmin):
    inlines =[
        ProfileInline,
    ]

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)