# Generated by Django 2.2.4 on 2019-09-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("utils", "0005_add_accordion_snippet")]

    operations = [
        migrations.CreateModel(
            name="StepSnippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "admin_title",
                    models.CharField(
                        help_text="The title value is only used to identify the snippet in the admin interface ",
                        max_length=255,
                    ),
                ),
                ("heading", models.CharField(max_length=500)),
                ("link_url", models.URLField(blank=True)),
                ("link_title", models.CharField(blank=True, max_length=125)),
            ],
        )
    ]