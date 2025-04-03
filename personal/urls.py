from django.urls import path
from personal import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("hobbies", views.hobbies, name="hobbies"),
    path("personal/", views.personal, name="personal"),
    path("post/<int:post_id>/", views.post, name="post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
