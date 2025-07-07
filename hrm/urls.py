from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('app.urls')),
    path('admin', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Intelligent HRM Admin"
admin.site.site_title = "Intelligent HRM Admin Portal"
admin.site.index_title = "Welcome to Intelligent HRM Admin Portal"