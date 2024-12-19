from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
# Create your views here.
from .models import News, newsComment
from .forms import newsCommentForm,ContactForm,NewsLetterForm
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def index_view(request,**kwargs):
    #return render(request, 'home/index.html')
#def blog_view(request,cat_name=None,author_username=None):
    news = News.objects.filter(status=1 , published_date__lte=timezone.now())
    if kwargs.get('cat_name') is not None:
    #if cat_name:
        news = news.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author') is not None:
    #if author_username:
        news = news.filter(author =kwargs['author'])
    if kwargs.get('tag_name') is not None:
    #if tag_name:
        news = news.filter(tags__name=kwargs['tag_name'])
    news = Paginator(news,3)

    
    comments = newsComment.objects.filter(approved=True).order_by('-created_date')
    
    try:        
        page_number = request.GET.get('page')
        news = news.get_page(page_number)
    except PageNotAnInteger:
        news = news.get_page(1)
    except EmptyPage:
        news = news.get_page(1)
    context = {'news': news , 'comments' : comments}
    return render(request, 'home/index.html', context=context)


def about_view(request):
    return render(request, 'home/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)            
            contact.save()
            messages.add_message(request, messages.SUCCESS ,"Your data is saved correctly") 
            return render(request, 'home/contact.html', {'form':form })
        else:
            messages.add_message(request, messages.ERROR, "Your data is NOT saved!", {'form':form })
            return render(request, 'home/contact.html', {'form':form })

    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form':form })


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


def index_search(request):
    news = News.objects.filter(status=1 , published_date__lte=timezone.now())  
    if request.method == 'GET':
        if s := request.GET.get('s'):
            news = news.filter(content__contains = s)    
    context = {'news': news}
    return render(request, 'home/index.html', context=context)


def newsletter_view(request):    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS ,"Your email is saved successfully")
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR ,"Your email is not saved!")
            return HttpResponseRedirect('/')
    else:
        form = NewsLetterForm() 
        return render(request, 'home/index.html', {'form': form})