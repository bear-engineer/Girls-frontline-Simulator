from django.urls import path
from ..api import Dolls, DollDetail, postman, TestView

app_name = 'api_dolls'
urlpatterns = [
    path('all/', Dolls.as_view()),
    path('all/<int:pk>/', DollDetail.as_view()),
    path('effect_formula/', postman),
    path('test/', TestView.as_view()),
]
