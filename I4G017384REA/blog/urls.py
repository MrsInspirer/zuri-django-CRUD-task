from django.urls import path
from .views import Blog

app_name = "blog"

urlpatterns = [

    path("", Blog.PostListView.as_view(), name="all"),
    path("create/", Blog.PostCreateView.as_view(), name="post_create"),
    path("delete/<slug:slug>", Blog.PostDeleteView.as_view(), name="post_delete"),
    path("update/<slug:slug>", Blog.PostUpdateView.as_view(), name="post_update"),
    path("read/<slug:slug>", Blog.PostDetailView.as_view(), name="post_detail"),
]