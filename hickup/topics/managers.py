from django.db import models
from django.db.models import Q


class TopicsQuerySet(models.QuerySet):
    def all(self, **kwargs):
        return self.filter(**kwargs)

    def all_private(self, **kwargs):
        return self.filter(private_reply=True, **kwargs)

    def all_latest(self, **kwargs):
        return self.order_by('-created')

    def all_helpful(self, **kwargs):
        return self.filter(helpful=True)

class TopicsManager(models.Manager):
    
    def get_queryset(self, **kwargs):
        return TopicsQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()

    def all_private(self):
        return self.get_queryset().all_private()

    def all_latest(self):
        return self.get_queryset().all_latest()

    def all_helpful(self):
        return self.get_queryset().all_helpful()
