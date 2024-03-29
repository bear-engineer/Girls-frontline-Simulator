from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import api_urls as api
from .. import views

urlpatterns = [
                  path('members/', include('members.urls')),
                  # path('dolls/', include('tactical_dolls.urls')),
                  path('admin/', admin.site.urls),
                  path('api/', include(api)),
                  path('', views.index, )

              ] + static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
