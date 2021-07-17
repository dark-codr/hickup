from __future__ import absolute_import

# development system imports
import datetime
import os
import random
import uuid
from datetime import date, timedelta
from decimal import Decimal


from hickup.users.managers import UsersManager


# from django.db.models.fields.related import ManyToManyField

# Third partie imports
from countries_plus.models import Country
from django_resized import ResizedImageField
from dateutil import relativedelta
# django imports
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db.models import (
    CASCADE,
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    GenericIPAddressField,
    ImageField,
    OneToOneField,
    SlugField,
    TextChoices,
    ManyToManyField,
    TextField,
    URLField,
    UUIDField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField


class User(AbstractUser):
    """Default user for hickup."""
    MODERATOR = 'MODERATOR'
    QUESTIONER = 'QUESTIONER'
    HELPER = 'HELPER'
    ROLE_CHOICES = (
        ('', 'Role'),
        (MODERATOR, 'Moderator'),
        (QUESTIONER, 'Questioner'),
        (HELPER, 'Helper'),
    )

    #: First and last name do not cover name patterns around the globe
    role = CharField(_("User Role"), choices=ROLE_CHOICES, default=QUESTIONER, blank=True, null=True, max_length=255)

    objects = UsersManager()

    def fullname(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.username}"
        return fullname

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

























# Image upload folders
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def profile_image(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "user-profile-photo/{new_filename}/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )

class Profile(TimeStampedModel):
    SEX = (
    ("", "Gender"),
    ("Male", "MALE"),
    ("Female", "FEMALE"),
    )

    MARITAL = (
        ("", "Marital"),
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorced", "Divorced"),
        ("Seperated", "Seperated"),
    )

    STATES = (
        ("", "States"),
        ("Abia", "Abia"),
        ("Adamawa", "Adamawa"),
        ("Akwa Ibom", "Akwa Ibom"),
        ("Anambra", "Anambra"),
        ("Bauchi", "Bauchi"),
        ("Bayelsa", "Bayelsa"),
        ("Benue", "Benue"),
        ("Borno", "Borno"),
        ("Cross River", "Cross River"),
        ("Delta", "Delta"),
        ("Ebonyi", "Ebonyi"),
        ("Enugu", "Enugu"),
        ("Edo", "Edo"),
        ("Ekiti", "Ekiti"),
        ("Gombe", "Gombe"),
        ("Imo", "Imo"),
        ("Jigawa", "Jigawa"),
        ("Kaduna", "Kaduna"),
        ("Kano", "Kano"),
        ("Katsina", "Katsina"),
        ("Kebbi", "Kebbi"),
        ("Kogi", "Kogi"),
        ("Kwara", "Kwara"),
        ("Lagos", "Lagos"),
        ("Nasarawa", "Nasarawa"),
        ("Niger", "Niger"),
        ("Ogun", "Ogun"),
        ("Ondo", "Ondo"),
        ("Osun", "Osun"),
        ("Oyo", "Oyo"),
        ("Plateau", "Plateau"),
        ("Rivers", "Rivers"),
        ("Sokoto", "Sokoto"),
        ("Taraba", "Taraba"),
        ("Yobe", "Yobe"),
        ("Zamfara", "Zamfara"),
    )


    # REGEX Expressions for validation
    SSN_REGEX = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4}\\d{4}$)"
    NUM_REGEX = "^[0-9]*$"
    ABC_REGEX = "^[A-Za-z]*$"


    user = OneToOneField(User, on_delete=CASCADE, related_name='profile')

    # symmetrical meaning, if i follow you, you cant automatically follow me back
    follows = ManyToManyField('self', related_name='followed_by', symmetrical=False) 


    image = ResizedImageField(size=[500, 300], quality=75, crop=['middle', 'center'], upload_to=profile_image, force_format='JPEG')
    gender = CharField(_("Gender"), max_length=7, blank=True, null=True, choices=SEX)
    dob = DateField(_("Date of Birth"), blank=True, null=True)
    marital = CharField(
        _("Marital Status"), max_length=10, blank=True, null=True, choices=MARITAL
    )
    phone_no = CharField(_("Phone Number"), blank=True, null=True, max_length=13)

    @property
    def age(self):
        TODAY = datetime.date.today()
        if self.dob:
            return "%s" % relativedelta.relativedelta(TODAY, self.dob).years
        else:
            return None

    def __str__(self):
        return self.user.fullname

    class Meta:
        managed = True
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created", "-modified"]

# this creates the user profile with a user and makes referencing the user.profile easier
User.profile = property(lambda u:Profile.objects.get_or_create(user=u)[0])