from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, User
from .forms import PostForm 
from django.contrib.auth.decorators import login_required

@login_required 
def post_list(request):
    """
    View to display a list of published blog posts
    AND handle creation of new posts via POST request.
    """
    posts = Post.objects.all().order_by('-published_at')
    form = PostForm() 

    if request.method == "POST":
        
        form = PostForm(request.POST) 
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author =  User.objects.get(username='roshanchokhani')
            Post.publish(post)
           
          
            return redirect('post_list') 
     
    context = {
        'posts': posts,
        'form': form, 
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    """View to display a single blog post.""" 
    post = get_object_or_404(Post, pk=pk, published_at__lte=timezone.now())
    
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context) 




