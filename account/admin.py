from django.contrib import admin
#****003
from .models import Profile,wholesale_pass

#****003
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
@admin.register(wholesale_pass)
class Profilepass(admin.ModelAdmin):
    list_display = ['wpass']
