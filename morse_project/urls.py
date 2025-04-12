from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('morse_app.urls')),
]

# Only if using file uploads (image upload for OCR)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)