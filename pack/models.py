from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from trainer.models import Trainer


class GymPack(models.Model):
    alphanumeric = RegexValidator(r'^[\-\ 0-9a-zA-Z]*$',
                                  'Only alphanumeric characters and (-) are allowed.')

    s = [("a", "Active"), ("i", "InActive")]

    name = models.CharField(max_length=50,
                            unique=True,
                            validators=[alphanumeric],
                            help_text="Maximum 50 Characters")

    days = models.PositiveIntegerField(validators=[MaxValueValidator(99999),
                                                   MinValueValidator(1), ],
                                       help_text="Days only valid from 1 to 99999")

    fee = models.PositiveIntegerField(validators=[MaxValueValidator(999999999),
                                                  MinValueValidator(1), ],
                                      help_text="Fee only valid from 1 to 999999999")

    status = models.CharField(max_length=1, choices=s, default="a")

    def __str__(self):
        return self.name


class PersonalPack(models.Model):
    alphanumeric = RegexValidator(r'^[\-\ 0-9a-zA-Z]*$',
                                  'Only alphanumeric characters and (-) are allowed.')

    s = [("a", "Active"), ("i", "InActive")]

    name = models.CharField(max_length=50,
                            unique=True,
                            validators=[alphanumeric],
                            help_text="Maximum 50 Characters")

    days = models.IntegerField(validators=[MaxValueValidator(99999),
                                           MinValueValidator(1), ],
                               help_text="Days only valid from 0 to 99999")

    session = models.IntegerField(validators=[MaxValueValidator(99999),
                                              MinValueValidator(1), ],
                                  help_text="Days only valid from 0 to 99999")

    duration_of_session = models.FloatField(validators=[MaxValueValidator(24),
                                                        MinValueValidator(1), ],
                                            help_text="Days only valid from 0 to 99999")

    fee = models.IntegerField(validators=[MaxValueValidator(999999999),
                                          MinValueValidator(1), ],
                              help_text="Fee only valid from 0 to 999999999")

    status = models.CharField(max_length=1, choices=s, default="a")

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Days(models.Model):
    s = [("SUN", "Sunday"),
         ("MON", "Monday"),
         ("TUE", "Tuesday"),
         ("WED", "Wednesday"),
         ("THU", "Thursday"),
         ("FRI", "Friday"),
         ("SAT", "Saturday"), ]

    days = models.CharField(max_length=3, choices=s, unique=True)

    def __str__(self):
        return self.days


class SpecialPack(models.Model):
    s = [("a", "Active"), ("i", "InActive")]

    name = models.CharField(max_length=50, unique=True)

    session = models.IntegerField(validators=[MaxValueValidator(99999),
                                              MinValueValidator(1), ],
                                  help_text="Days only valid from 0 to 99999")

    fee = models.IntegerField(validators=[MaxValueValidator(999999999),
                                          MinValueValidator(1), ],
                              help_text="Fee only valid from 0 to 999999999")

    duration_of_session = models.FloatField(validators=[MaxValueValidator(24),
                                                        MinValueValidator(1), ],
                                            help_text="Days only valid from 0 to 99999")

    time_from = models.TimeField()

    time_to = models.TimeField()

    maximum_seats = models.IntegerField(validators=[MaxValueValidator(99999),
                                                    MinValueValidator(1), ],
                                        help_text="Days only valid from 0 to 99999")

    days = models.ManyToManyField(Days)

    status = models.CharField(max_length=1, choices=s, default="a")

    trainer = models.ManyToManyField(Trainer)
