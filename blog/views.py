from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post,PostComment
from django.utils import timezone
from blog.forms import PostCommentForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from django.contrib import messages



def blog_view(request,**kwargs):
#def blog_view(request,cat_name=None,author_username=None):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())
    if kwargs.get('cat_name') is not None:
    #if cat_name:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
    #if author_username:
        posts = posts.filter(author__username =kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
    #if tag_name:
        posts = posts.filter(tags__name=kwargs['tag_name'])
    posts = Paginator(posts,3)

    
    comments = PostComment.objects.filter(approved=True).order_by('-created_date')
    
    try:        
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts, 'comments' : comments}
    return render(request, 'blog/blog.html', context=context)

def single_view(request, post_id):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS ,"Your Comment Submitted") 
        else:
            messages.add_message(request, messages.ERROR, "Your Comment did not Submitted!", {'form':form })

        
    
    current_post = get_object_or_404(Post,status=1, id = post_id)    
    current_post.counted_views += 1
    current_post.save()

    all_posts = Post.objects.all().order_by('published_date').filter(status=1, published_date__lte=timezone.now())
    current_index = list(all_posts).index(current_post)
    previous_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None
    comments = PostComment.objects.filter(post_id =current_post.id,approved=True)

    form = PostCommentForm()
    context = {
        'current_post': current_post,
        'previous_post': previous_post,
        'next_post': next_post,
        'comments' : comments,
        'form' : form,
    }
    if not current_post.login_require:        
        return render(request, 'blog/single.html', context)
    else:
        if not request.user.is_authenticated:         
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            return render(request, 'blog/single.html', context)
        

def blog_search(request):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())  
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)    
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context=context)

