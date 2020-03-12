from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from rca.utils.models import BasePage


class ShortCoursePage(BasePage):
    template = "patterns/pages/standardpages/information_page.html"

    introduction = models.TextField(blank=True)

    search_fields = BasePage.search_fields + [
        index.SearchField("introduction"),
    ]

    content_panels = BasePage.content_panels + [
        FieldPanel("introduction"),
    ]
