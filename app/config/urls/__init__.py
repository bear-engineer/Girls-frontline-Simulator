from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import api_urls as api

urlpatterns = [
                  path('members/', include('members.urls')),
                  path('dolls/', include('tactical_dolls.urls')),
                  path('admin/', admin.site.urls),
                  path('api/', include(api)),

              ] + static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
