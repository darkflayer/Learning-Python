from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.post_list), name="post_list"),
    path("create/", login_required(views.post_create), name="post_create"),
    path("update/<int:post_id>/", login_required(views.post_update), name="post_update"),
    path("delete/<int:post_id>/", login_required(views.post_delete), name="post_delete"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("register/", views.register_view, name="register"),
    path("post/<int:post_id>/", views.post_details, name="post_details"),
]
