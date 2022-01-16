from rest_framework import routers

from apps.books.api.views import BooksViewSet

router = routers.DefaultRouter()

router.register(r'books', BooksViewSet)

urlpatterns = router.urls
