# Generated by Django 2.2.4 on 2019-09-09 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("programmes", "0028_remove_gallery_title")]

    operations = [
        migrations.RemoveField(model_name="programpagerelatedstaff", name="link_text")
    ]