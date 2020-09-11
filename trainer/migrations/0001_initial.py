# Generated by Django 2.2.3 on 2019-07-16 07:33

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_one', models.CharField(help_text='+911234567890', max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:  '+999999999'. Up to 10 digits allowed. Country Code with (+) Sign Required", regex='^\\+?1?\\d{12}$')])),
                ('mobile_two', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:  '+999999999'. Up to 10 digits allowed. Country Code with (+) Sign Required", regex='^\\+?1?\\d{12}$')])),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='f', max_length=1)),
                ('address', models.TextField(blank=True, help_text='Maximum 300 Characters only', max_length=300)),
                ('profession', models.CharField(blank=True, help_text='Maximum 30 Characters only', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('marriage', models.DateField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, default='default.png', upload_to='profile_pics_trainer')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
