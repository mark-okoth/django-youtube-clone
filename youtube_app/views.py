from django.shortcuts import render
from . models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class postListView(ListView):
    model = Post
    template_name = 'resourses/index.html'
    context_object_name = 'posts'
    ordering = ['-date']

class postDetailView(DetailView):
    model = Post
    template_name = 'resourses/post_detail.html'



def about(request):
    return render(request, 'resourses/about.html')