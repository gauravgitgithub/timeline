"""timeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.core.views import homepage, signup
from apps.feeds.views import feeds, search
from apps.userprofile.views import (
    userprofile,
    edit_profile,
    follow_user,
    unfollow_user,
    followers,
    follows,
)
from django.contrib.auth import views
from apps.feeds.api import add_new_post, like_feed

urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup/", signup, name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "login/", views.LoginView.as_view(template_name="core/login.html"), name="login"
    ),
    # Feed
    path("feeds/", feeds, name="feeds"),
    path("search/", search, name="search"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("u/<str:username>/", userprofile, name="userprofile"),
    path("u/<str:username>/followers/", followers, name="followers"),
    path("u/<str:username>/follows/", follows, name="follows"),
    path("u/<str:username>/follow/", follow_user, name="follow_user"),
    path("u/<str:username>/unfollow/", unfollow_user, name="unfollow_user"),
    # API
    path("api/add_post", add_new_post, name="add_new_post"),
    path("api/like_feed", like_feed, name="like_feed"),
    # Admim
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
