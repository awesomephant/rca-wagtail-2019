# Generated by Django 2.2.4 on 2019-09-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("utils", "0006_add_step_snippets")]

    operations = [
        migrations.CreateModel(
            name="FeeDisclaimerSnippet",
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
                ("text", models.TextField(blank=True)),
                (
                    "admin_title",
                    models.CharField(
                        help_text="The title value is only used to identify the snippet in the admin interface ",
                        max_length=255,
                    ),
                ),
            ],
        )
    ]
