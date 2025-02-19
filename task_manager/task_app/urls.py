from django.urls import path
from . import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path(
        "task/add/",
        views.TaskCreate.as_view(),
        name="task-add",
    ),
    path(
        "task/<int:pk>/",
        views.TaskUpdate.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        views.TaskDelete.as_view(),
        name="task-delete",
    ),
]