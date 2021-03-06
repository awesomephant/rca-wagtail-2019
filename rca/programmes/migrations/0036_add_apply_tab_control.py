# Generated by Django 2.2.4 on 2019-09-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("programmes", "0035_increase_character_counts")]

    operations = [
        migrations.AddField(
            model_name="programmepage",
            name="disable_apply_tab",
            field=models.BooleanField(
                default=0,
                help_text="This setting will remove the apply tab from the programme page",
            ),
        )
    ]
