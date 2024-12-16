from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
# Create your views here.
from .models import News, newsComment
from .forms import newsCommentForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def index_view(request,**kwargs):
    #return render(request, 'home/index.html')

#def blog_view(request,cat_name=None,author_username=None):
    news = News.objects.filter(status=1 , published_date__lte=timezone.now())
    if kwargs.get('cat_name') is not None:
    #if cat_name:
        news = news.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
    #if author_username:
        news = news.filter(author__username =kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
    #if tag_name:
        news = news.filter(tags__name=kwargs['tag_name'])
    news = Paginator(news,3)

    
    #comments = Comment.objects.filter(approved=True)
    
    try:        
        page_number = request.GET.get('page')
        news = news.get_page(page_number)
    except PageNotAnInteger:
        news = news.get_page(1)
    except EmptyPage:
        news = news.get_page(1)
    context = {'news': news}
    return render(request, 'home/index.html', context=context)


def about_view(request):
    return render(request, 'home/about.html')


def contact_view(request):
    return render(request, 'home/contact.html')

def single_news(request,news_id):
    current_news = get_object_or_404(News,status=1, id = news_id)    
    current_news.counted_views += 1
    current_news.save()

    all_news = News.objects.all().order_by('published_date').filter(status=1, published_date__lte=timezone.now())
    current_index = list(all_news).index(current_news)
    previous_news = all_news[current_index - 1] if current_index > 0 else None
    next_news = all_news[current_index + 1] if current_index < len(all_news) - 1 else None
    comments = newsComment.objects.filter(news_id =current_news.id,approved=True)

    form = newsCommentForm()
    context = {
        'current_news': current_news,
        'previous_news': previous_news,
        'next_news': next_news,
        'comments' : comments,
        'form' : form,
    }
            
    return render(request, 'home/news.html', context)
    

def common_data(request):
       return {
        'name' : "Poorya",
        'surname' : "Fayazi",
        'email1' : "fayazipoorya@gmail.com",
        'email2' : "poorya189@gmail.com",
        'phone1' : "+989190104604",
        'phone2' : "+989937272005",
        'city' : "Tehran",
        'country' : "IRAN",
       }


