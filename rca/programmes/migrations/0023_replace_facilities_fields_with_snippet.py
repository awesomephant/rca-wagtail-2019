# Generated by Django 2.2.4 on 2019-09-05 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0004_replace_facilities_fields_with_snippet"),
        ("programmes", "0022_amend_requirements_body_field"),
    ]

    operations = [
        migrations.RemoveField(model_name="programmepage", name="facilities_copy"),
        migrations.RemoveField(model_name="programmepage", name="facilities_intro"),
        migrations.AddField(
            model_name="programmepage",
            name="facilities_snippet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="utils.FacilitiesSnippet",
            ),
        ),
    ]