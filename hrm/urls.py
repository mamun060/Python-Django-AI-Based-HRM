from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('app.urls')),
    path('admin', admin.site.urls),
]

admin.site.index_title = "Intellegent HRM"
admin.site.site_header = "Intellegent HRM"
admin.site.site_title = "Intellegent HRM"
