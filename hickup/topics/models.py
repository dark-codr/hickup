from __future__ import absolute_import

# development system imports
import datetime
from hickup.topics.managers import TopicsManager
import os
import random
import uuid
from datetime import date, timedelta
from decimal import Decimal

# Third partie imports
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
    TextField,
    URLField,
    UUIDField,
)
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField

User = get_user_model()

# Create your models here.
# Image upload folders
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def topics_image(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "topic-uploads/{new_filename}/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )


class Topics(TimeStampedModel):
    author = ForeignKey(User, on_delete=CASCADE, related_name="usertopic")
    title = CharField(_('Topic Title'), unique=True, max_length=500, null=True, blank=False)
    slug = SlugField(_('Topic Slug'), max_length=500, unique=True, null=True, blank=True)
    content = HTMLField(_('Topic Content'), null=True, blank=True)
    private_reply = BooleanField(default=False)
    email_me = BooleanField(default=False)
    helpful = BooleanField(default=False)

    objects = TopicsManager()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        ordering = ["-created", "-modified"]

    def get_absolute_url(self):
        return reverse("topics:detail", kwargs={"slug": self.slug})
    

class TopicImages(TimeStampedModel):
    topic = ForeignKey(Topics, on_delete=CASCADE, related_name="topicimage")
    image = ResizedImageField(size=[2000, 1222], quality=75, crop=['middle', 'center'], upload_to=topics_image, force_format='JPEG')

    def __str__(self):
        return self.topic.title
    
