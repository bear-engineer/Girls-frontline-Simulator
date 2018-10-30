from django.urls import path
from .. import api_views

urlpatterns = [
    path('list/', api_views.DollList.as_view()),
    path('simulator/', api_views.SimulatorView.as_view()),
]
