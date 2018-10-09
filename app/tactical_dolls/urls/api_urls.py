from django.urls import path
from ..api import Dolls, DollDetail

app_name = 'api_dolls'
urlpatterns = [
    path('all/', Dolls.as_view()),
    path('all/<int:pk>/', DollDetail.as_view())
]
