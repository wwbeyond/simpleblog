from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse



# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def test(request):
    return  render(request, 'blog/test1.html',{})

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

# def post_new(request):
#   if request.method=="POST":
#     form=PostForm(request.POST)
#     if form.is_valid():
#       post=form.save(commit=False)
#       post.author=request.user
#       post.save()
#       return redirect('blog.views.post_detail',pk=post.pk)
#   else:
#      form=PostForm()
#   return render(request,'blog/post_edit.html',{"form":form})

