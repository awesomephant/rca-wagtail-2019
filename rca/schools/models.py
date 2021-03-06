from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.search import index

from rca.utils.models import BasePage


class SchoolsAndResearchPage(BasePage):
    template = "patterns/pages/schools/schools_and_research_page.html"
    description = models.TextField(blank=True)
    content_panels = BasePage.content_panels + [FieldPanel("description")]
    search_fields = BasePage.search_fields + [index.SearchField("description")]

    api_fields = [APIField("description")]
