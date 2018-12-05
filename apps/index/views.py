from django.shortcuts import render,HttpResponse
from .models import LoveFitness
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# localhost:8888
'''首页 + 分页显示'''
def index(request):
    types = LoveFitness.objects.all().order_by('-datetime')
    paginator = Paginator(types, 20)

    types_count = LoveFitness.objects.count()
    maxNum = types_count // 20 + 1

    pageNum = request.GET.get('page',1)


    pageBlogs = paginator.get_page(pageNum)  # 将获取的第几页的文章列表值给赋值,get方法会自动处理异常
    currentPageNum = pageBlogs.number  # 获取当前页码

    # 页面范围  显示 分页时的 结果， 就是如果有多个分页，不完全显示，就显示4个页面
    #   获取当前页码和 当前页码的前后两页
    page_range = list(range(max(currentPageNum - 2, 1), currentPageNum)) + list(range(currentPageNum, min(currentPageNum + 2, paginator.num_pages) + 1))

    #   加上省略页码
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    try:
        contacts = paginator.page(pageNum)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    category = LoveFitness.objects(s_cate='健身知识')[0]
    jszs = category.s_cate
    category = LoveFitness.objects(s_cate='健身励志')[0]
    jslz = category.s_cate
    category = LoveFitness.objects(s_cate='健身热点')[0]
    jsrd = category.s_cate
    category = LoveFitness.objects(s_cate='健身投稿')[0]
    jstg = category.s_cate
    category = LoveFitness.objects(s_cate='健身音乐')[0]
    jsyy = category.s_cate
    category = LoveFitness.objects(s_cate='30天挑战计划')[0]
    thirty_days = category.s_cate
    category = LoveFitness.objects(s_cate='减脂塑形')[0]
    jzsx = category.s_cate
    category = LoveFitness.objects(s_cate='增肌增重')[0]
    zjzz = category.s_cate
    category = LoveFitness.objects(s_cate='健身打卡')[0]
    jsdk = category.s_cate
    category = LoveFitness.objects(s_cate='哑铃锻炼')[0]
    yl = category.s_cate
    category = LoveFitness.objects(s_cate='训练计划')[0]
    xljh = category.s_cate
    category = LoveFitness.objects(s_cate='胸部')[0]
    xb = category.s_cate
    category = LoveFitness.objects(s_cate='背部')[0]
    bb = category.s_cate
    category = LoveFitness.objects(s_cate='腿部')[0]
    tb = category.s_cate
    category = LoveFitness.objects(s_cate='肩部')[0]
    jb = category.s_cate
    category = LoveFitness.objects(s_cate='手臂')[0]
    sb = category.s_cate
    category = LoveFitness.objects(s_cate='腹部')[0]
    fb = category.s_cate
    category = LoveFitness.objects(s_cate='臀部')[0]
    tbu = category.s_cate
    category = LoveFitness.objects(s_cate='健身营养')[0]
    jsyyzs = category.s_cate
    category = LoveFitness.objects(s_cate='健身视频')[0]
    jssp = category.s_cate
    category = LoveFitness.objects(s_cate='健身美女')[0]
    jsmn = category.s_cate
    category = LoveFitness.objects(s_cate='肌肉男')[0]
    jrn = category.s_cate

    return render(request,"index.html",{'pageNum':str(pageNum),'contacts':contacts,'maxNum':maxNum,'pageBlogs':pageBlogs,'page_range':page_range,
                                        'jszs':jszs,'jslz':jslz,'jsrd':jsrd,'jstg':jstg,'jsyy':jsyy,
                                        '30days': thirty_days, 'jzsx':jzsx, 'zjzz':zjzz, 'jsdk':jsdk, 'yl':yl, 'xljh':xljh,
                                        'xb':xb,'bb':bb,'tb':tb,'jb':jb,'sb':sb,'fb':fb,'tbu':tbu,
                                        'jsyyzs': jsyyzs, 'jssp': jssp, 'jsmn': jsmn, 'jrn': jrn,
                                        })
