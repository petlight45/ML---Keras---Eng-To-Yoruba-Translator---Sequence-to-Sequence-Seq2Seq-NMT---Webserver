from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"public/", include("app.api.public.urls.secure"), name="api_public_secure")

]
