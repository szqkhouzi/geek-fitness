from django.shortcuts import render
from .models import fitness

# Create your views here.

def detail(request):
    date = request.GET.get('date')
    title = request.GET.get('title')
    types = fitness.objects(date=date,title=title)[0]
    title = types.title
    print('*'* 50,title)
    # date = types.date
    content_html = types.content_html

    context = {
        'title':title,
        # 'date':date,
        'content_html':content_html
    }
    return render(request,'detail.html',context)
