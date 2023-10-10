from django.urls import re_path
from . import consumers
websocket_urlpatterns=[
    re_path(r"ws/postid/\d+/$",consumers.tasksConsumer.as_asgi()),
    re_path(r"ws/taskid/\d+/$",consumers.comsConsummer.as_asgi()),
    #re_path("ws/chat/lobby/",consumers.ChatConsumer.as_asgi()),
]