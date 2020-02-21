# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime
from Bean.models import *
from django.shortcuts import render
from django.contrib.auth.models import User

def  checkPublisher(request):
    yhm_into = request.POST['yhm']
    mm_into = request.POST['mm']
    context = {}
    page_count = request.session['page_count']  #标记当前页数
    try:
        user = Xwfbyhb.objects.get(yhm = yhm_into)
        if user.mm == mm_into:
            return render(request , 'publisherConsole.html')  #检查成功 , 进入新闻编辑界面
        else:
            context['publisher_state'] = 0
            context['publisher_info'] = '用户名或密码错误'
            return render(request , 'hello.html' ,context)
    except Exception as ex:
        print("publisherServer.py 出错: %s" % ex)
        context['publisher_state'] = 0
        context['publisher_info'] = '用户名或密码错误'
        context['page_count'] = page_count
        url = request.session.get('releaseNewReturn')
        if url is None:
            url = 'http://127.0.0.1:8000/hello/1'  #定位到首页
        else:
            url = 'http://127.0.0.1:8000'+url
        context['url'] = url
        return render(request , 'hello.html' , context)
