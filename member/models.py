from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from PIL import Image


class Member(models.Model):
    # Mobile Number Validator
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$',
                                 message="Phone number must be entered in the format: "
                                         " '+999999999'. Up to 10 digits allowed. "
                                         "Country Code with (+) Sign Required")

    # Choices for Sex List
    s = [("m", "Male"), ("f", "Female")]

    # Fields of Member Model
    first_name = models.CharField(max_length=50, blank=False, null=False)

    last_name = models.CharField(max_length=50, blank=False, null=False)

    mobile_one = models.CharField(unique=True,
                                  validators=[phone_regex],
                                  max_length=13,
                                  help_text="+911234567890")  # validators should be a list

    mobile_two = models.CharField(validators=[phone_regex],
                                  max_length=13,
                                  blank=True)

    sex = models.CharField(max_length=1, choices=s, default="f")

    address = models.TextField(blank=True,
                               max_length=300,
                               help_text="Maximum 300 Characters only")

    profession = models.CharField(blank=True,
                                  max_length=30,
                                  help_text="Maximum 30 Characters only")

    email = models.EmailField(max_length=100, blank=True)

    marriage = models.DateField(null=True, blank=True)

    dob = models.DateField(null=True, blank=True)

    pic = models.ImageField(default="default.png",
                            upload_to="profile_pics",
                            blank=True)

    date_joined = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super(*args, **kwargs).save(*args, **kwargs)
        img = Image.open(self.pic.path)
        img.thumbnail((286, 180), Image.ANTIALIAS)
        img.save(self.pic.path)