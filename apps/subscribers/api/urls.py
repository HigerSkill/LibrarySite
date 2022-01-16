from rest_framework import routers

from apps.subscribers.api.views import SubscribersViewSet

router = routers.DefaultRouter()

router.register(r'subscribers', SubscribersViewSet)

urlpatterns = router.urls
