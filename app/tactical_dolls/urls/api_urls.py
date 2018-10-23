from django.urls import path
from ..api import Dolls, DollDetail, DollFormula

app_name = 'api_dolls'
urlpatterns = [
    path('', Dolls.as_view()),
    path('<int:pk>/', DollDetail.as_view()),
    path('formula/', DollFormula.as_view()),
]
