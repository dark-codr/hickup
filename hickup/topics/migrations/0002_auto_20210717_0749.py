# Generated by Django 3.1.13 on 2021-07-17 06:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Topic Content'),
        ),
    ]