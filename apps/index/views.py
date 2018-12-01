from django.shortcuts import render,HttpResponse
from .models import fitness
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
import time
# Create your views here.

# localhost:8888

# '''首页'''
# def index(request):
#     '''显示首页'''
#     # 获取文章分类信息，通过date降序展示
#     types = fitness.objects.all().order_by('-date')
#     context = {'types':types}
#     return render(request,'index.html',context)


'''首页 + 分页显示'''
def index(request):

    types = fitness.objects.all()

    paginator = Paginator(types, 20)

    types_count = fitness.objects.count()
    maxNum = types_count // 20 + 1

    pageNum = request.GET.get('page',1)
    try:
        contacts = paginator.page(pageNum)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request,"index.html",{'pageNum':str(pageNum),'contacts':contacts,'maxNum':maxNum})


'''测试'''
def index_test_views(request):
    # result = fitness.objects.filter(s_cate= '健身知识').count()
    result = fitness.objects.filter(date='2018年11月16日').values_list('b_cate','title')
    print('qqq',result)
    return render(request,'index.html')




