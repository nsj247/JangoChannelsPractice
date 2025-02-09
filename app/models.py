from django.db import models
from app.mixins import ChannelLayerGroupSendMixin
from django.db.models.signals import post_save, post_delete
from django.urls import reverse

# Create your models here.
class Post(ChannelLayerGroupSendMixin, models.Model):
    CHANNEL_LAYER_GROUP_NAME = 'liveblog'

    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ["-id"] # 쿼리셋의 디폴트 정렬

def post__on_post_save(instance: Post, created: bool, **kwras):
    if created:
        message_type ="liveblog.post.created"
    else:
        message_type = "liveblog.post.updated"

    post_id = instance.pk 
    post_partial_url = reverse("post_partial", args=[post_id])

    instance.channel_layer_group_send({
       "type": message_type,
       "post_id": post_id,
       "post_partial_url": post_partial_url 
    })

def post__on_post_delete(instance: Post, **kwargs):
    post_id = instance.pk 

    instance.channel_layer_group_send({
        "type": "liveblog.post.deleted",
        "post_id": post_id
    })

post_save.connect(
    post__on_post_save,
    sender=Post,
    dispatch_uid="post__on_post_save"
)

post_delete.connect(
    post__on_post_delete,
    sender=Post,
    dispatch_uid="post__on_post_delete"
)