from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "task_app/index.html"

    def get_queryset(self):
        return Task.objects.filter()

    def get_context_data(self):
        context = super().get_context_data()
        return context

class TaskCreate(CreateView):
    model = Task
    fields = [
        "title",
        "description",
        "due_at",
        "status",
    ]

    def get_initial(self):
        initial_data = super(TaskCreate, self).get_initial()
        return initial_data

    def get_context_data(self):
        context = super(TaskCreate, self).get_context_data()
        context["title"] = "Create a new task"
        return context

    def get_success_url(self):
        return reverse("index")

class TaskUpdate(UpdateView):
    model = Task
    fields = [
        "title",
        "description",
        "due_at",
        "status",
    ]

    def get_context_data(self):
        context = super(TaskUpdate, self).get_context_data()
        context["title"] = "Edit task"
        return context

    def get_success_url(self):
        return reverse("index")

class TaskDelete(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(TaskDelete, self).get_context_data()
        return context