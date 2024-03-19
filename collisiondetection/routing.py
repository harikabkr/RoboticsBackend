# routing.py
from django.urls import re_path

from . import consumers

# configuring Django Channels to route WebSocket connections to the 
# NotificationConsumer class when the URL matches 'ws/notifications/'.
websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]
