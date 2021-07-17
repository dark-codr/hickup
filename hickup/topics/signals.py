from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from hickup.utils.unique_slug_generator import unique_slug_generator

from .models import Topics, Category

def pre_save_topic_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_topic_slug, sender=Topics)