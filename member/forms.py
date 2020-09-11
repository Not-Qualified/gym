from django import forms
from django.forms import ModelForm
from .models import Member
from datetime import datetime


class MemberCreateForm(ModelForm):
    s = [("m", "Male"), ("f", "Female")]
    sex = forms.ChoiceField(choices=s, widget=forms.RadioSelect)

    mobile_one = forms.CharField(max_length=13,
                                 label="Mobile Number",
                                 required=True)

    mobile_two = forms.CharField(max_length=13,
                                 label="Mobile Number",
                                 required=False)

    YEARS = [y for y in range(1900, datetime.now().year + 1)]

    # marriage = forms.DateField(label="Marriage Anniversary",
    #                            required=False,
    #                            widget=forms.SelectDateWidget(years=YEARS))

    # dob = forms.DateField(label="Date of Birth",
    #                       required=False,
    #                       widget=forms.SelectDateWidget(years=YEARS))

    marriage = forms.DateField(required=False, widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    dob = forms.DateField(required=False, widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    pic = forms.ImageField(label="Upload Profile Picture", required=False)

    class Meta:
        model = Member
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
