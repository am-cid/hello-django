from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("listing/create/", views.listing_create, name="listing_create"),
    path("listing/<int:pk>/", views.listing_detail, name="listing_detail"),
    path("listing/<int:pk>/edit/", views.listing_update, name="listing_update"),
    path("listing/<int:pk>/delete/", views.listing_delete, name="listing_delete"),
]
