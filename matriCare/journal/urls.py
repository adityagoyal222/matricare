from django.conf.urls import url
from . import views

app_name = "journal"

urlpatterns = [
    url(r'personal/', views.LogListView.as_view(), name="log_list"),
    url(r'shared/(?P<pk>[-\w]+)/$', views.ShareJournalView.as_view(), name="shared_journal"),
    url(r'redirect/', views.redirectToJournalView, name="redirect"),
]