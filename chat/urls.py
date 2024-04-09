from django.urls import path, include
from chat import views

app_name = "chat"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.room_new, name="room_new"),
    path("<str:room_name>/chat/", views.room_chat, name="room_chat"),
    path("<str:room_name>/chat/")
]
