from django.urls import path, include

urlpatterns = [
    # 유저 정보
    path('members/', include('members.urls.api_urls')),
    # 전술 인형
    path('doll/', include('doll.urls.api_urls')),
    # path('equip/', include('tactical_equips.urls.api_urls')),
]
