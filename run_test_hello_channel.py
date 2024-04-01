import os
import asyncio
import django
from channels.layers import get_channel_layer

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()

async def main():
    message_dict = {'content': 'world'}

    channel_layer = get_channel_layer()
    channel_layer.send('hello', message_dict)

    await channel_layer.send('hello', message_dict)
    response_dict = await channel_layer.receive('hello')
    is_equal = message_dict == response_dict
    print("송신/수신 데이터가 같습니까?", is_equal)

asyncio.run(main())