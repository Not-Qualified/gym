from django.urls import path
from .views import GymPackCreate, PersonalPackCreate, SpecialPackCreate


urlpatterns = [
    path("gym/create/", GymPackCreate.as_view(), name="gym-pack-create"),
    path("personal/create/", PersonalPackCreate.as_view(), name="personal-pack-create"),
    path("special/create/", SpecialPackCreate.as_view(), name="special-pack-create"),
]
