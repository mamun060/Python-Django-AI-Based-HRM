from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('app.urls')),
    path('admin', admin.site.urls),
]


admin.site.site_header = "Intelligent HRM Admin"
admin.site.site_title = "Intelligent HRM Admin Portal"
admin.site.index_title = "Welcome to Intelligent HRM Admin Portal"