# Generated by Django 2.2.3 on 2019-08-06 20:56

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0003_remove_navigationsettings_secondary_navigation")
    ]

    operations = [
        migrations.AlterField(
            model_name="navigationsettings",
            name="footer_navigation",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "link",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("url", wagtail.core.blocks.URLBlock(required=False)),
                                (
                                    "page",
                                    wagtail.core.blocks.PageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Leave blank to use the page's own title, required if using a URL",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                help_text="Multiple columns of footer links with optional header.",
            ),
        )
    ]
