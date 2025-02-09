from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

    @property
    def chat_group_name(self):
        return self.make_chat_group_name(room=self)

    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "caht-%s" % (room_pk or room.pk)
