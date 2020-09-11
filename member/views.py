from django.shortcuts import render, redirect
from .forms import MemberCreateForm
from django.contrib import messages
from django.views.generic import View, ListView, DetailView
from .models import Member


class Create(View):
    form = MemberCreateForm()
    extra_context = {"form": form}
    template_name = "member/create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.extra_context)

    def post(self, request, *args, **kwargs):
        self.form = MemberCreateForm(request.POST, request.FILES, *args, **kwargs)
        if self.form.is_valid():
            self.form.save(*args, **kwargs)
            messages.success(request, f"Account for {self.form.cleaned_data['first_name']} "
                                      f"has been created, Login to Continue ...")

            return redirect("member-list")
        else:
            return render(request, self.template_name, {"form": self.form})


class MemberList(ListView):
    model = Member
    template_name = "member/member_list.html"


class MemberDetail(DetailView):
    model = Member
    template_name = "member/member_detail.html"
