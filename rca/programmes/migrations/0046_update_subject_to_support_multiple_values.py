# Generated by Django 2.2.9 on 2020-01-14 03:45

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("programmes", "0045_change_prgm_type_to_fk_rel")]

    operations = [
        migrations.RemoveField(model_name="programmepage", name="subject"),
        migrations.CreateModel(
            name="ProgrammePageSubjectPlacement",
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
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subjects",
                        to="programmes.ProgrammePage",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subjects",
                        to="programmes.Subject",
                    ),
                ),
            ],
        ),
    ]