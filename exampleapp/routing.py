from django.urls import re_path
from django_htmx_live_trigger.consumers import HTMXEventsConsumer

websocket_urlpatterns = [
    re_path(r"ws/events/(?P<group_name>\w+)/$", HTMXEventsConsumer.as_asgi()),
]