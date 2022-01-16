from apps.users.api.views import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', UsersViewSet)

urlpatterns = router.urls
