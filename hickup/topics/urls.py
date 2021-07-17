from django.urls import path

from hickup.topics.views import (
    topics_detail_view,
    topics_list_view,
    topics_create_view,
    topics_update_view,
    topics_delete_view,
)

app_name = "topics"
urlpatterns = [
    path("", view=topics_list_view, name="list"),
    path("create/", view=topics_create_view, name="create"),
    path("<slug>/", view=topics_detail_view, name="detail"),
    path("<slug>/update/", view=topics_update_view, name="update"),
    path("<slug>/delete/", view=topics_delete_view, name="delete"),
]
