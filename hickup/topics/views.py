from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    FormMixin,
    UpdateView
)


from .models import Topics
from .forms import TopicForm

# Create your views here.
class TopicListView(ListView):
    model = Topics
    template_name = 'topics/list.html'
    ordering = '-created'
    context_object_name = 'topics'
    paginate_by = 20


topics_list_view = TopicListView.as_view()

class TopicDetailView(DetailView):
    model = Topics
    template_name = 'topics/detail.html'
    context_object_name = 'topic'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

topics_detail_view = TopicDetailView.as_view()


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topics
    template_name = 'topics/create.html'
    success_message = "Your topic has been created successfully"
    form_class = TopicForm

    def from_valid(self, form):
        form = super().form_valid(form)
        form.author = self.request.user

    def get_success_url(self):
        return self.object.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.object


topics_create_view = TopicCreateView.as_view()


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    model = Topics
    template_name = 'topics/update.html'
    context_object_name = 'topic'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_message = "Your topic has been updated successfully"
    fields = ["title", "content"]

    def get_success_url(self):
        return self.object.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.object


topics_update_view = TopicUpdateView.as_view()

class TopicDeleteView(LoginRequiredMixin, DeleteView):
    model = Topics
    context_object_name = 'topic'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_message = "Your topic has been deleted successfully"
    success_url = reverse_lazy('topics:list')

    def get_object(self):
        return self.object


topics_delete_view = TopicDeleteView.as_view()

