# Generated by Django 2.2.4 on 2019-09-23 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("utils", "0008_movel_link_to_snippet"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProgrammeSettings",
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
                    "disable_apply_tab",
                    models.BooleanField(
                        default=0,
                        help_text="This setting will remove the apply tab from all programme pages",
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Site",
                    ),
                ),
            ],
            options={"verbose_name": "Programme settings"},
        )
    ]
