from django.shortcuts import render, redirect
from .forms import TrainerCreateForm
from django.contrib import messages
from django.views.generic import View, ListView, DetailView
from .models import Trainer


class Create(View):
    form = TrainerCreateForm()
    extra_context = {"form": form}
    template_name = "trainer/create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.extra_context)

    def post(self, request, *args, **kwargs):
        self.form = TrainerCreateForm(request.POST, request.FILES, *args, **kwargs)
        if self.form.is_valid():
            self.form.save(*args, **kwargs)
            messages.success(request, f"Account for {self.form.cleaned_data['first_name']} "
            f"has been created, Login to Continue ...")

            return redirect("trainer-list")
        else:
            return render(request, self.template_name, {"form": self.form})


class TrainerList(ListView):
    model = Trainer
    template_name = "trainer/trainer_list.html"


class TrainerDetail(DetailView):
    model = Trainer
    template_name = "trainer/trainer_detail.html"
