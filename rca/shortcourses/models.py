from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel

from rca.shortcourses.access_planit import AccessPlanitXML
from rca.utils.blocks import AccordionBlockWithTitle
from rca.utils.models import BasePage


class ShortCoursePage(BasePage):
    parent_page_types = ["guides.GuidePage"]
    template = "patterns/pages/shortcourses/short_course.html"

    hero_image = models.ForeignKey(
        "images.CustomImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    introduction = models.CharField(max_length=500, blank=True)
    introduction_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    video_caption = models.CharField(
        blank=True,
        max_length=80,
        help_text="The text dipsplayed next to the video play button",
    )
    video = models.URLField(blank=True)
    body = RichTextField(blank=True)
    about = StreamField(
        [("accordion_block", AccordionBlockWithTitle())],
        blank=True,
        verbose_name=_("About the course"),
    )

    access_planit_course_id = models.CharField(max_length=10)

    content_panels = BasePage.content_panels + [
        MultiFieldPanel([ImageChooserPanel("hero_image")], heading=_("Hero")),
        MultiFieldPanel(
            [
                FieldPanel("introduction"),
                ImageChooserPanel("introduction_image"),
                FieldPanel("video"),
                FieldPanel("video_caption"),
                FieldPanel("body"),
            ],
            heading=_("Course Introduction"),
        ),
        StreamFieldPanel("about"),
        FieldPanel("access_planit_course_id"),
    ]

    def get_access_planit_data(self):
        data = AccessPlanitXML(course_id=self.access_planit_course_id)
        return data.get_data()

    def _format_booking_bar(self, access_planit_data):
        """ Booking bar messaging with the next course data available
        Find the next course date marked as status='available' and advertise
        this date in the booking bar. If there are no courses available, add
        a default message."""

        booking_bar = {
            "message": "Applications are now closed",
            "action": "Register your interest for upcoming dates",
        }
        # If there are no dates the booking link should go to a form, not open
        # a modal
        if self.access_planit_course_id:
            booking_bar["link"] = (
                "https://rca-verdant-staging.herokuapp.com/short-courses/regi"
                f"ster-your-interest/?course_id={self.access_planit_course_id}"
            )

        if access_planit_data:
            for key, date in enumerate(access_planit_data):
                if date["status"] == "Available":
                    booking_bar["message"] = "Next course starts"
                    booking_bar["date"] = access_planit_data[key]["start_date"]
                    booking_bar[
                        "action"
                    ] = f"Book now from \xA3{access_planit_data[key]['cost']}"
                    booking_bar["link"] = None
                    booking_bar["modal"] = "booking-details"
                    break
        return booking_bar

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        access_planit_data = self.get_access_planit_data()
        context["booking_bar"] = self._format_booking_bar(access_planit_data)
        context["access_planit_data"] = access_planit_data
        return context
