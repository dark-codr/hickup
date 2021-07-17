from django.urls import path

from hickup.feeds.views import (
    feeds_detail_view,
    feeds_list_view,
    feeds_update_view,
    feeds_delete_view,
)

app_name = "topics"
urlpatterns = [
    path("", view=feeds_list_view, name="list"),
    path("<slug>/", view=feeds_detail_view, name="detail"),
    path("<slug>/update/", view=feeds_update_view, name="update"),
    path("<slug>/delete/", view=feeds_delete_view, name="delete"),
]
