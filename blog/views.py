from django.shortcuts import render

# Create your views here.


def blog_view(request):
    return render(request, 'blog/blog.html')

def single_view(request):
    context ={"title":"blog title" ,"contenct":"blog contenct" ,'author':'Poorya fayazi'}
    return render(request, 'blog/single.html',context=context)