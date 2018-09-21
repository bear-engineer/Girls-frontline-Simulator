from django.urls import path
from ..api import Dolls

app_name = 'api_dolls'
urlpatterns = [
    path('all/', Dolls.as_view())
]
