from rest_framework.routers import DefaultRouter
from .views import JobDescriptionViewSet, ApplicationViewSet

router = DefaultRouter()
router.register("job-descriptions", JobDescriptionViewSet, basename="job-description")
router.register("applications", ApplicationViewSet, basename="application")

urlpatterns = router.urls