from django.urls import path
from chat import consumers

websocket_urlpatterns = [
    path("ws/chat/test/chat/", consumers.ChatConsumer.as_asgi()),
]