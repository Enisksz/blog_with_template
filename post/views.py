from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostCreateModelForm,PostUpdateModelForm
from comment.forms import CommentAddModel
from category.models import Category


from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def post_list_view(request):
    q = request.GET.get('q','')
    if q:
        queryset = (Q(categories__name__icontains=q))
        posts = Post.objects.filter(queryset).distinct().order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    categories = Category.objects.all()
    context = {
        'posts':posts,
        'categories':categories
    }
    return render(request,'pages/posts.html',context)


def post_detail_page(request,slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    comments = post.comments.all()
    

    if request.method=='POST':
        comment_add_form = CommentAddModel(request.POST)
        if comment_add_form.is_valid():
            comment = comment_add_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # olduğumuz sayfada kalmamızı sağlar.
    else:
        comment_add_form = CommentAddModel()
    
    context = {
        'post':post,
        'categories':categories,
        'comments':comments,
        'comment_add_form':comment_add_form
    }
    return render(request,'pages/post_detail.html',context)


@login_required(login_url='/')
def post_update(request,slug):
    post = get_object_or_404(Post,slug=slug,author=request.user)
    form  = PostUpdateModelForm(request.POST or None,files=request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('post-detail',slug=post.slug)

    context = {'form':form}
    return render(request,'pages/post_update.html',context)

@login_required(login_url='/')
def post_create(request):
    form = PostCreateModelForm(request.POST or None,files=request.FILES or None)
    
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

        form.save_m2m()
        
        return redirect('post-detail',slug=post.slug)
    context = {'form':form}
    return render(request,'pages/post-create.html',context)

@login_required(login_url='/')
def post_delete(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if (request.user == post.author) or (request.user.is_authenticated):
        post.delete()
    else:
        return f'Yetkisiz kullanıcı'
    return redirect('/')
