from django.urls import reverse
from django.views.generic import CreateView
from .models import GymPack, PersonalPack, SpecialPack
from django import forms


class GymPackCreate(CreateView):
    model = GymPack
    template_name = "pack/gym_pack_create.html"
    fields = ["name", "days", "fee", "status"]

    def get_success_url(self):
        return reverse("trainer-list")


class PersonalPackCreate(CreateView):
    model = PersonalPack
    template_name = "pack/personal_pack_create.html"
    fields = ["name",
              "days",
              "session",
              "duration_of_session",
              "fee",
              "status",
              "trainer"]

    def get_success_url(self):
        return reverse("trainer-list")


class SpecialPackCreate(CreateView):
    model = SpecialPack
    template_name = "pack/special_pack_create.html"
    time_from = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "time"}))
    fields = ["name",
              "session",
              "fee",
              "duration_of_session",
              "time_from",
              "time_to",
              "maximum_seats",
              "days",
              "trainer",
              "status", ]

    def get_success_url(self):
        return reverse("trainer-list")
