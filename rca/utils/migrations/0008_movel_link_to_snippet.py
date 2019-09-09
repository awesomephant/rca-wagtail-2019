# Generated by Django 2.2.4 on 2019-09-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("utils", "0007_add_fee_disclaimer_snippet")]

    operations = [
        migrations.AddField(
            model_name="facilitiessnippet",
            name="link_title",
            field=models.CharField(blank=True, max_length=125),
        ),
        migrations.AddField(
            model_name="facilitiessnippet",
            name="link_url",
            field=models.URLField(blank=True),
        ),
    ]
