from django.contrib.auth import views as auth_views
from django.urls import path
from member.views import Create, MemberList, MemberDetail


urlpatterns = [
    path("login/", 
        auth_views.LoginView.as_view(template_name="member/home.html"), 
        name="member-login"),
    path("create/", Create.as_view(), name="member-create"),
    path("list/", MemberList.as_view(), name="member-list"),
    path("view/<int:pk>", MemberDetail.as_view(), name="member-detail"),
]
