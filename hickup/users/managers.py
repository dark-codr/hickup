from django.db import models
from django.db.models import Q


class UsersQuerySet(models.QuerySet):
    def all_members(self, **kwargs):
        return self.filter(is_active=True, is_superuser=False, **kwargs)

    def all_staff(self, **kwargs):
        return self.filter(is_active=True, is_staff=True, **kwargs)

class UsersManager(models.Manager):
    
    def get_queryset(self, **kwargs):
        return UsersQuerySet(self.model, using=self._db)

    def all_members(self):
        return self.get_queryset().all_members()

    def all_staff(self):
        return self.get_queryset().all_staff()

    def number_of_members(self):
        return self.get_queryset().all_members().count()
