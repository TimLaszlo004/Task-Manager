from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Count

class TaskListView(ListView):
    model = Task
    template_name = "task_app/index.html"

    def get_queryset(self):
        queryset = Task.objects.all()
        filter_status = self.request.GET.get('filter_status', None)
        filter_due_date = self.request.GET.get('filter_due_date', None)
        sort_val = self.request.GET.get('sort', None)
        
        if filter_status:
            queryset = queryset.filter(status=filter_status)
        
        if filter_due_date:
            queryset = queryset.filter(due_at=filter_due_date)
        
        if sort_val:
            queryset = queryset.order_by(sort_val)
        else:
            queryset = queryset.order_by('title')
        
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['filter_status'] = self.request.GET.get('filter_status', '')
        context['filter_due_date'] = self.request.GET.get('filter_due_date', '')
        context['sort'] = self.request.GET.get('sort', '')
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

    def form_valid(self, form):
        due_at = form.cleaned_data.get('due_at')
        if due_at and due_at < timezone.now():
            form.add_error('due_at', ValidationError("Due date cannot be in the past."))
            return self.form_invalid(form)
        return super().form_valid(form)

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

    def form_valid(self, form):
        due_at = form.cleaned_data.get('due_at')
        if due_at and due_at < timezone.now():
            form.add_error('due_at', ValidationError("Due date cannot be in the past."))
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")

class TaskDelete(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(TaskDelete, self).get_context_data()
        return context

def smart_task_suggestions(request):
    similar_tasks = Task.objects.values('title').annotate(count=Count('title')).order_by('-count')[:5]
    similar_suggestions = [task['title'] for task in similar_tasks]

    completed_tasks = Task.objects.filter(status='completed').values('title').annotate(count=Count('title')).order_by('-count')[:5]
    completed_suggestions = [task['title'] for task in completed_tasks]

    suggestions = {
        'similar_tasks': similar_suggestions,
        'completed_tasks': completed_suggestions,
    }

    return JsonResponse(suggestions)