import requests
from bs4 import BeautifulSoup as Soup
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        url = (
            "https://rca.accessplanit.com/accessplansandbox/services/WebIntegration.asmx/GetCoursesPackage?companyID"
            "=ROYALC9RCH&courseIDs=731014&venueIDs=&categoryIDs="
        )
        response = requests.get(url)
        soup = Soup(response.text, "lxml")
        for date in soup.findAll("dates"):
            print(date)
        context["ap_data"] = soup

        return context
