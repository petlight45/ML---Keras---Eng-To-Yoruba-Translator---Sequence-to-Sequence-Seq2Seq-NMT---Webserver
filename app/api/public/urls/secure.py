from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from ..views import secure as views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("ml", views.MLViewSet, basename="ml")

urlpatterns = router.urls
