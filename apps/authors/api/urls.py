from rest_framework import routers

from apps.authors.api.views import AuthorsViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorsViewSet)

urlpatterns = router.urls
