from django.views.generic.edit import CreateView

from .models import Post

# Create your views here.

class PostCreateView(CreateView):
    model=Post
    fields= ['title','slug','author','body','publish','created','updated','status',]
    template_name=["base.html","post_confirm_delete.html","post_details.html","post_forms.html","post_list.html",]