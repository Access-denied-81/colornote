from django.urls import re_path
from game.consumers import DrawingConsumer

websocket_urlpatterns = [
    re_path(r'ws/drawing',DrawingConsumer.as_asgi())
]