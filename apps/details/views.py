from django.shortcuts import render
from .models import LoveFitness

# Create your views here.

def detail(request):
    date = request.GET.get('date','')
    title = request.GET.get('title','')
    types = LoveFitness.objects(date=date,title=title)[0]
    title = types.title
    content_html = types.content_html
    content_html = content_html[:-381]

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
    return render(request,'detail.html',{'title':title,'content_html':content_html,
                                        'jszs':jszs,'jslz':jslz,'jsrd':jsrd,'jstg':jstg,'jsyy':jsyy,
                                        '30days': thirty_days, 'jzsx':jzsx, 'zjzz':zjzz, 'jsdk':jsdk, 'yl':yl, 'xljh':xljh,
                                        'xb':xb,'bb':bb,'tb':tb,'jb':jb,'sb':sb,'fb':fb,'tbu':tbu,
                                        'jsyyzs': jsyyzs, 'jssp': jssp, 'jsmn': jsmn, 'jrn': jrn,
                                        })
