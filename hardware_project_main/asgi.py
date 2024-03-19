"""
ASGI config for hardware_project_main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from collisiondetection.routing import websocket_urlpatterns as collisiondetection_websocket_urlpatterns
from channels.layers import get_channel_layer  # Add this import
from asgiref.sync import async_to_sync


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hardware_project_main.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            collisiondetection_websocket_urlpatterns
        )
    ),
})

def notify_clients_about_message(timestamp, description, saved_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("viewagent_group", {
        "type": "receive",
        "data": {
            "conversation": "obstacle detected",
            "type": "receive",
            "timestamp": timestamp,
            "description": description,
            "id": saved_id,
        }
    })
