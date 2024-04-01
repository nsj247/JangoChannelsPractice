import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
# 아래 임포트 경로는 실제 앱 이름과 routing.py 파일의 위치에 따라 달라질 수 있습니다.
import app.routing
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # 앱 이름이 'your_app_name'이고, 해당 앱 안에 'routing.py' 파일이 있어야 합니다.
    "websocket": URLRouter(
        app.routing.websocket_urlpatterns + chat.routing.websocket_urlpatterns
    )
})