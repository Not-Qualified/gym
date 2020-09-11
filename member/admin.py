from django.contrib import admin
from .models import Member
from django.contrib.admin import ModelAdmin


class MemberAdmin(ModelAdmin):
    list_display = ["first_name", "last_name", "mobile_one"]


admin.site.register(Member, MemberAdmin)
