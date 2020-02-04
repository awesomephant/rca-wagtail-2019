# Generated by Django 2.2.9 on 2019-12-18 15:16

import django.db.models.deletion
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_customimage_file_hash"),
        ("programmes", "0038_add_overview_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="programmeindexpage",
            name="contact_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="programmeindexpage",
            name="contact_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.CustomImage",
            ),
        ),
        migrations.AddField(
            model_name="programmeindexpage",
            name="contact_url",
            field=models.URLField(blank=True, verbose_name="Contact URL"),
        ),
        migrations.AddField(
            model_name="programmeindexpage",
            name="search_placeholder_text",
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name="programmeindexpage",
            name="introduction",
            field=wagtail.core.fields.RichTextField(),
        ),
    ]