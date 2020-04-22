from django.shortcuts import render,redirect,get_object_or_404

from rest_framework.generics import CreateAPIView,ListAPIView

from django.views.generic import ListView
# Create your views here.
from .serializers import PostSerializer
from .forms import PostForm
from .models import post

from taggit.models import Tag


NUM_COMMON_TAGS = 5

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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['common_tags'] = post.tags.most_common()[:NUM_COMMON_TAGS]
        return context


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = post.objects.filter(tags=tag)

    context = {
        'tag':tag,
        'object_list':posts,
    }
    return render(request, 'feed/post_list.html', context)