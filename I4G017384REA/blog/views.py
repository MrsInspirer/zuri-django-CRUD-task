from django.urls import reverse_lazy
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.

class PostCreateView(CreateView):
    model=Post
    fields= "__all__"
    template_name="base.html"

class PostDeleteView(DeleteView):
    model=Post
    fields="__all__"
    template_name="post_confirm_delete.html"
    success_url= reverse_lazy('blog:all')

class PostDetailView(DetailView):
    model=Post
    fields="__all__"
    template_name="post_details.html"
    success_url= reverse_lazy('blog:all')

    
class PostUpdateView(UpdateView):
    model=Post
    fields="__all__"
    template_name="update_forms.html"
    success_url=reverse_lazy('blog:all')

class PostListView(ListView):
    model=Post
    fields="__all__"
    template_name="post_list.html"
    success_url= reverse_lazy('blog:all')
    






