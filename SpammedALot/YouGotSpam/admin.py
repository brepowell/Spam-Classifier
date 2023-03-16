from django.contrib import admin

# Register your models here.

from .models import Email
from .models import Profile

# @admin.register(Email)
# class emailAdmin(admin.ModelAdmin):
#     list_display = ['owner', 'header', 'body', 'isSpam']

# @admin.register(Profile)
# class profileAdmin(admin.ModelAdmin):
#     list_display = ['name']
