# Generated by Django 2.2.9 on 2020-01-13 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("programmes", "0043_programmetype_description")]

    operations = [
        migrations.AddField(
            model_name="programmepage",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="programmes.Subject",
            ),
        )
    ]