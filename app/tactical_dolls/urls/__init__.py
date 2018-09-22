from django.urls import path

from tactical_dolls.views import Update

app_name = 'dolls'
urlpatterns = [
    path('update/', Update.as_view(), name='dolls-update'),

]
