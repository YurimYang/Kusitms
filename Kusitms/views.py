from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts' : posts}
    
    return render(request, template_name = 'list.html', context = ctx)

def post_detail(request, pk):
    post = Post.objects.get(id = pk)
    ctx = {'post' : post}
    
    return render(request, template_name = 'detail.html', context = ctx)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        ctx = {'form' : form}
        if form.is_valid():
            form.save()
            return redirect('Kusitms:list')
        
    else : 
        form = PostForm()
    return render(request, 'create.html', {'form' : form})

def post_delete(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.delete()
    return redirect('Kusitms:list')


def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save()
            return redirect('Kusitms:detail', pk)
    else :
        form = PostForm(instance = post)
        ctx = {'form' : form}

        return render(request, template_name = 'create.html', context = ctx)