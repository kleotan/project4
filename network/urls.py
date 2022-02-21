
from django.urls import path

from . import views

urlpatterns = [
    path("", views.NetworkHome.as_view(), name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('post/<int:post_pk>/', views.ShowPost.as_view(), name='post'),
    path("add_post", views.AddPost.as_view(), name = "add_post")
]
