from django import forms
from django.forms import ModelForm
from .models import Trainer


class TrainerCreateForm(ModelForm):
    s = [("m", "Male"), ("f", "Female")]

    sex = forms.ChoiceField(choices=s, widget=forms.RadioSelect)

    mobile_one = forms.CharField(max_length=13,
                                 label="Mobile Number",
                                 required=True)

    mobile_two = forms.CharField(max_length=13,
                                 label="Mobile Number",
                                 required=False)

    marriage = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}),
                               required=False)

    dob = forms.DateField(label="Date of Birth :",
                          widget=forms.widgets.DateInput(attrs={"type": "date"}),
                          required=False)

    address = forms.CharField(required=False,
                              widget=forms.widgets.Textarea(attrs={"rows": "3"}))

    pic = forms.ImageField(label="Upload Profile Picture", required=False)

    class Meta:
        model = Trainer
        fields = ["first_name",
                  "last_name",
                  "sex",
                  "mobile_one",
                  "mobile_two",
                  "email",
                  "address",
                  "profession",
                  "marriage",
                  "dob",
                  "pic", ]
