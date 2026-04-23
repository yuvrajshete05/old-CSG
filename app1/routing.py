# C:\app1\routing.py

from django.urls import re_path # Use re_path for regex-based URL matching

from . import consumers

websocket_urlpatterns = [
    # This pattern matches ws://<host>/ws/livechat/
    # It points to your LiveChatConsumer in app1
    re_path(r'ws/livechat/$', consumers.LiveChatConsumer.as_asgi()),
]