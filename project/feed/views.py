from django.shortcuts import render,redirect

from rest_framework.generics import CreateAPIView,ListAPIView

from django.views.generic import ListView
# Create your views here.
from .serializers import PostSerializer
from .forms import PostForm
from .models import post

# class CreatePostView(CreateAPIView):

#     queryset = post.objects.all()
#     serializer_class = PostSerializer

def CreatePostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed:list-posts')
    else:
        form = PostForm()
    return render(request,'feed/create_post.html',{'form':form})


class ListPostsView(ListView):
    model = post
    paginate_by = 10
    template_name = 'feed/post_list.html'
