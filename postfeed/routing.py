#create router for this, when ever websocket connection is done control will come here
from django.urls import re_path

from . import consumers


websocket_urlpatterns = [re_path(r"^ws/$", consumers.PostConsumer.as_asgi())]