# Generated by Django 2.2.9 on 2020-03-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("utils", "0010_update_help_texts")]

    operations = [
        migrations.CreateModel(
            name="ShortCourseDetailSnippet",
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
                    "snippet_type",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "FAQs"), (2, "T&Cs")]
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Used only in the CMS to identify this particular snippet.",
                        max_length=255,
                    ),
                ),
                ("url", models.URLField()),
            ],
        )
    ]
