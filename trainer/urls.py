from django.urls import path
from .views import Create, TrainerList, TrainerDetail


urlpatterns = [
    path("create/", Create.as_view(), name="trainer-create"),
    path("list/", TrainerList.as_view(), name="trainer-list"),
    path("view/<int:pk>", TrainerDetail.as_view(), name="trainer-detail"),
]
