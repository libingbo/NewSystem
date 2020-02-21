# -*- coding: utf-8 -*-
from .import userEngine
from .import newEngine
from django.http import HttpResponse
import datetime

def aa(request):
    user = userEngine.editorXWLLYHB()
    if user.addXWLLYH_browser('王浩博' , '820'  , '女' , '每天一部电视剧' , None , datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        return HttpResponse("<p>浏览者数据添加成功！</p>")
    else:
        return HttpResponse("<p>浏览者数据添加失败！</p>")


def deluser(request):
    user = userEngine.editorXWLLYHB()
    if user.delXWLLYH('太祖'):
        return HttpResponse("<p>数据删除成功</p>")
    else:
        return HttpResponse("<p>数据删除失败</p>")

def ediuser(request):
    user = userEngine.editorXWLLYHB();
    if user.ediXWLLYH_browser('王浩博' , '820' , '男' , '好的生活靠自己创造' , None ,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ):
        return HttpResponse("<p>编辑权限成功</p>")
    else:
        return HttpResponse("<p>编辑权限失败</p>")

def addnew(request):
    new = newEngine.editorXWNRB()
    if new.addXWNR_publisher( 2 , '时政新闻标题2' , '时政新闻导语2' , '时政新闻内容2' , 'bbp'):
        return HttpResponse("<p>张三插入新闻内容成功</p>")
    else:
        return HttpResponse("<p>张三插入新闻内容失败</p>")