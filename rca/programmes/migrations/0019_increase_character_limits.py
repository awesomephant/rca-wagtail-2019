# Generated by Django 2.2.4 on 2019-09-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("programmes", "0018_add_email_url_fields")]

    operations = [
        migrations.AlterField(
            model_name="programmepage",
            name="facilities_copy",
            field=models.TextField(
                blank=True, help_text="Max length 1000 characters", max_length=1000
            ),
        ),
        migrations.AlterField(
            model_name="programmepagefeeitem",
            name="introduction",
            field=models.CharField(
                blank=True,
                help_text="Extra information about the fee items",
                max_length=1000,
            ),
        ),
    ]