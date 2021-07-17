from django.contrib import admin
from .models import Topics, TopicImages

# Register your models here.

class TopicImagesInline(admin.StackedInline):
    model = TopicImages

class TopicAdmin(admin.ModelAdmin):
    inlines = [TopicImagesInline]

    class Meta:
        model = Topics

admin.site.register(Topics, TopicAdmin)