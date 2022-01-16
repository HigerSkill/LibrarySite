from django.urls import include, path
from rest_framework.authtoken import views

app_name = "api"


urlpatterns = [
    path('auth/', views.obtain_auth_token),
    path("users/", include("apps.users.api.urls")),
    path("authors/", include("apps.authors.api.urls")),
    path("books/", include("apps.books.api.urls")),
    path("subscribers/", include("apps.subscribers.api.urls")),
]
