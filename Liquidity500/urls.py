from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("adminLiquidity/", admin.site.urls),  # Include pwa.urls under root URL ('/')
    path(
        "", include("AppLiquidity.urls")
    ),  # Include Appjirani.urls under root URL ('/')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
