from django.contrib import admin
from .models import GymPack, PersonalPack, SpecialPack, Days
from django.contrib.admin import ModelAdmin


class GymPackAdmin(ModelAdmin):
    list_display = ["name", "days", "fee", "status"]


admin.site.register(GymPack, GymPackAdmin)


class PersonalPackAdmin(ModelAdmin):
    list_display = ["name", "days", "fee", "status"]


admin.site.register(PersonalPack, PersonalPackAdmin)


class SpecialPackAdmin(ModelAdmin):
    list_display = ["name", "fee", "status"]


admin.site.register(SpecialPack, SpecialPackAdmin)


class DaysAdmin(ModelAdmin):
    list_display = ["days"]


admin.site.register(Days, DaysAdmin)
