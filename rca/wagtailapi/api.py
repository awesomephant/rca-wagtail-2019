from wagtail.api.v2 import router

from rca.wagtailapi.endpoints import NavigationEndpoint, PagesAPIEndpoint

api_router = router.WagtailAPIRouter("wagtailapi")
api_router.register_endpoint("pages", PagesAPIEndpoint)
api_router.register_endpoint("navigation", NavigationEndpoint)