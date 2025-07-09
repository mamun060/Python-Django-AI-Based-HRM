from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('app.urls')),
<<<<<<< HEAD
    path("", include("attendance.urls")),
    path('admin', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
    path('admin', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 34accc8f6043820424f9169cdc62545edc287931

admin.site.site_header = "Intelligent HRM Admin"
admin.site.site_title = "Intelligent HRM Admin Portal"
admin.site.index_title = "Welcome to Intelligent HRM Admin Portal"