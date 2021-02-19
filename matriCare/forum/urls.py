from django.conf.urls import url
from . import views

app_name = "forum"

urlpatterns = [
    url(r'list/', views.PostListView.as_view(), name="post_list"),
    url(r'(?P<pk>[-\w]+)/$', views.PostDetailView.as_view(), name="post_detail")
]