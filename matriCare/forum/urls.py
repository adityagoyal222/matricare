from django.conf.urls import url
from . import views

app_name = "forum"

urlpatterns = [
    url(r'list/(?P<filter>[-\w]+)/$', views.PostListView.as_view(), name="post_list_latest"),
    url(r'list/(?P<filter>[-\w]+)/$', views.PostListView.as_view(), name="post_list_popular"),
    url(r'(?P<pk>[-\w]+)/$', views.PostDetailView.as_view(), name="post_detail")
]