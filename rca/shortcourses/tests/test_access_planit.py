import logging
import warnings
from unittest import mock

import requests
from django.conf import settings
from django.core.cache import cache
from django.core.management import call_command
from django.http.request import QueryDict
from django.test import TestCase
from requests.exceptions import Timeout

from rca.home.models import HomePage
from rca.shortcourses.access_planit import AccessPlanitXML, AccessPlanitXMLParser
from rca.shortcourses.models import ShortCoursePage

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", message="No directory at", module="whitenoise.base")


def mocked_fetch_data_from_xml(**kargs):
    with open("./rca/shortcourses/tests/test_data.xml", "r") as file:
        data = AccessPlanitXMLParser(xml=file.read())
        data = data.get_parsed_data()
    return data


class AccessPlanitXMLTest(TestCase):
    def setUp(self):
        self.expected_data = [
            {
                "course_date_id": "12086",
                "course_id": "731014",
                "cost": "1250",
                "start_date": "2020-03-27T09:00:00",
                "end_date": "2020-04-02T17:00:00",
                "spaces_available": "22",
                "status": "Available",
                "book_now_url": (
                    "https://rca.accessplanit.com/accessplansand"
                    "box/clientinput/course/coursebooker.aspx?coursedateid=12086"
                ),
                "enquire_url": (
                    "https://rca.accessplanit.com/accessplansand"
                    "box/clientinput/company/contactcompany.aspx?contacttype=8&"
                    "coursecalid=12086"
                ),
            },
            {
                "course_date_id": "12085",
                "course_id": "731014",
                "cost": "9000",
                "start_date": "2020-05-13T09:00:00",
                "end_date": "2020-05-19T17:00:00",
                "spaces_available": "22",
                "status": "Available",
                "book_now_url": (
                    "https://rca.accessplanit.com/accessplansand"
                    "box/clientinput/course/coursebooker.aspx?coursedateid=12085"
                ),
                "enquire_url": (
                    "https://rca.accessplanit.com/accessplansand"
                    "box/clientinput/company/contactcompany.aspx?contacttype=8&"
                    "coursecalid=12085"
                ),
            },
            {
                "course_date_id": "12071",
                "course_id": "731014",
                "cost": "1250",
                "start_date": "2020-07-20T09:00:00",
                "end_date": "2020-07-24T17:00:00",
                "spaces_available": "20",
                "status": "Available",
                "book_now_url": (
                    "https://rca.accessplanit.com/accessplansand"
                    "box/clientinput/course/coursebooker.aspx?coursedateid=12071"
                ),
                "enquire_url": (
                    "https://rca.accessplanit.com/accessplansand"
                    "box/clientinput/company/contactcompany.aspx?contacttype=8&"
                    "coursecalid=12071"
                ),
            },
        ]
        self.query = QueryDict(mutable=True)
        self.query.update(
            {
                "CompanyID": "ROYALC9RCH",
                "courseIDs": 1,
                "venueIDs": "",
                "categoryIDs": "",
            }
        )
        self.query = self.query.urlencode()

    def test_xml_fetch(self):
        """ Test the XML fetch responds. """
        response = requests.get(
            settings.ACCESS_PLANIT_XML_BASE_URL + self.query, timeout=5
        )
        self.assertEqual(response.status_code, 200)

    def test_xml_fetch_no_venue(self):
        """ Prove that you must pass blank values as parameters"""
        query = QueryDict(mutable=True)
        query.update({"CompanyID": "ROYALC9RCH", "courseIDs": 1})
        query = query.urlencode()
        response = requests.get(settings.ACCESS_PLANIT_XML_BASE_URL + query, timeout=5)
        self.assertEqual(response.text, """Missing parameter: venueIDs.\r\n""")
        self.assertEqual(response.status_code, 500)

    """ Patch the request module totally to force the timeout so we can test the
        result of the try/expect.

        Test here that data returned from a timeout is a empty dict
    """

    @mock.patch("rca.shortcourses.access_planit.requests.get")
    def test_data_if_timeout(self, mock_get):
        """ If a timeout is caught the xml_data should be an empty list"""
        # logging.disable(logging.CRITICAL)  # Don't log exceptions for tests... is this bad?
        mock_get.side_effect = Timeout
        data = AccessPlanitXML(course_id=1)
        xml_data = data.get_data()
        self.assertEqual(xml_data, [])

    def test_management_command_fetch_data(self):
        """ Test that xml with no dates goes in the cache as [] """
        for i in range(5):
            ShortCoursePage.objects.create(
                title=f"Short course {i}",
                path=str(i),
                depth="001",
                access_planit_course_id=i,
            )
        args = []
        opts = {}
        call_command("fetch_access_planit_data", *args, **opts)
        for i in range(5):
            cache_key = f"short_course_{i}"
            self.assertEqual(cache.get(cache_key), [])

    @mock.patch("rca.shortcourses.access_planit.requests.get")
    def test_page_renders_with_timeout(self, mock_get):
        logging.disable(
            logging.CRITICAL
        )  # Silences the timeout raised from mock when running the test
        """ If there is a timeout for the xml request when the page loads,
        ensure the page still renders with the empty data"""
        home_page = HomePage.objects.first()
        mock_get.side_effect = Timeout
        short_course_page = ShortCoursePage(
            title="Short course title", slug="short-course", access_planit_course_id="1"
        )
        home_page.add_child(instance=short_course_page)
        response = self.client.get("/short-course/")
        self.assertTemplateUsed(
            response, "patterns/pages/shortcourses/short_course.html"
        )
        self.assertContains(response, "Short course title")
        self.assertEqual(
            response.render().status_code, 200
        )  # will render 404 if there is an failure

    @mock.patch(
        "rca.shortcourses.access_planit.AccessPlanitXML.fetch_data_from_xml",
        side_effect=mocked_fetch_data_from_xml,
    )
    def test_page_renders_good_xml(self, mocked_fetch_data_from_xml):
        """ Test that the example xml file is passed through the parser and is set
        in cache, and when retrieved is what we expect """
        home_page = HomePage.objects.first()
        short_course_page = ShortCoursePage(
            title="Short course title", slug="short-course", access_planit_course_id="1"
        )
        home_page.add_child(instance=short_course_page)
        response = self.client.get("/short-course/")

        self.assertTemplateUsed(
            response, "patterns/pages/shortcourses/short_course.html"
        )
        self.assertContains(response, "Short course title")
        self.assertEqual(
            response.render().status_code, 200
        )  # will render 404 if there is an failure
        self.assertEqual(cache.get("short_course_1"), self.expected_data)

    def test_parsing(self):
        with open("./rca/shortcourses/tests/test_data.xml", "r") as file:
            data = file.read()
            parser = AccessPlanitXMLParser(xml=data)
            parsed_data = parser.get_parsed_data()
            self.assertEqual(parsed_data, self.expected_data)
