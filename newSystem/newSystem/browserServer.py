# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime
from Bean.models import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator  #django自带的分页功能
from django.db.models import Q   #搜索功能 模糊查询 要用到

#完成用户登录
def loginCheck(request):
    info = {}
    yhm_sel = request.POST['yhm']
    mm_sel = request.POST['mm']
    user_name = request.session.get('user_name')
    page_count = request.session['page_count']
    url = request.session.get('releaseNewReturn')  #取出 暂存的 请求url
    url = "http://127.0.0.1:8000"+ url
    info['url'] = url
    if user_name is None  or yhm_sel != user_name:  #session不存在用户名, 或者session里存的用户名和提交来的用户名不相同 , 没有登录
        try:
            user = Xwllyhb.objects.get(yhm = yhm_sel)
            if mm_sel == user.mm: #数据库用户存在, 并且密码相同
                 #one = User.objects.create_user(username=yhm_sel, password=mm_sel)
                 print("用户已经存储-----------------------------------------------------------")
                 info['login_message'] = '登录成功! 用户已经储存'
                 request.session['user_name'] = yhm_sel
                 info['login_state'] = 1  #1表示登录成功
                 info['return_home'] = '返回首页'
                 return render(request, 'login.html', info)
            else:
                info['login_state'] = 0 #前端不跳转页面
                info['login_message'] = '您输入的密码不正确'
                print('密码不正确--------------------------------------')
                return render(request , 'login.html' , info)
        except Exception as ex:
            print(ex)
            info['login_state'] = 0 #前端不跳转页面
            info['login_message'] = '您输入的用户不存在'
            return render(request, 'login.html', info)
    else:  #当前用户已经登录
        info['login_message'] = '您已经登录,无需重复登录'
        info['login_state'] = 2  #用户已经登录过了
        info['return_home'] = '返回首页'
        return render(request, 'login.html', info)


#完成用户注册
def  registerInto(request):
    info = {}
    page_count = request.session['page_count']
    url = request.session.get('releaseNewReturn')  # 取出 暂存的 请求url
    url = "http://127.0.0.1:8000" + url
    info['url'] = url
    try:
        yhm_into = request.POST['yhm']
        mm_into = request.POST['mm']
        user = Xwllyhb(yhm = yhm_into , mm = mm_into)
        user.save()
    except Exception as ex:
        print(ex)
        info['register_state'] = 0  #注册失败 标记为0
        info['register_message'] = '注册失败 , 请仔细检查您的用户名和密码'
        return render(request, 'register.html', info)
    else:  #注册成功, 跳转到home.html
        info['register_state'] = 1  # 前端检查是否注册成功的标记 成功为 1
        info['return_home'] = '返回首页'
        info['register_message'] = '注册成功! 欢迎来到毕设新闻大家庭~~~'
        return render(request , 'register.html' ,  info)


#浏览者首次进入首页时 , 取出新闻内容表数据 , 到前端进行渲染
def showNew(request , pindex):
    request.session['page_count'] = pindex    #把当前请求的页数存到session里 , 以后用直接取
    new_list = Xwnrb.objects.all()
    for i  in new_list:
        print(i.fbzyhm)
        print(type(i.fbzyhm))  #查询时fzbyhm 是一个Xwfbyhb , 可能是有外键关系, 所以取值是取的一个带where的表 , i,fbzyhm,yhm是用户名
    paginator = Paginator(new_list, 5)  # 实例化Paginator, 每页显示5条数据
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:  # 如果有返回在值，把返回值转为整数型
        int(pindex)
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    print(page)
    context = {'page':page}
    context['urlKind'] = 'hello'
    ################################################################
    # releaseNewReturn 变量记录了url的一次状态 , 存储在session中 , 当用户执行发布新闻验证失败后 ,要返回上次浏览的地方 , 这个变量代表上次浏览的位置
    # 他在publisherServer.py 文件的checkPublisher函数中使用 , 相关的变量是url
    # 在本文件的registerInto函数中也用到   对应变量url
    # 在本文件的loginCheck也用到了  对应变量url
    releaseNewReturn = request.get_full_path()
    print(releaseNewReturn)
    request.session['releaseNewReturn'] = releaseNewReturn
    ################################################################
    return render(request, 'hello.html', context)

#用户阅读单条新闻----操作:用户在首页点击阅读按钮后
def show_one_new(request , id_one):
    context ={}
    try:
        new = Xwnrb.objects.get(id = id_one)
        #print(new.bt)    属性是按modles.py文件定义的属性, 所以是小写, 不是按数据库表的字段(不是大写)
        #print('--------------------------------------------------------------------------------------')
        #将用户浏览的新闻记录 记录到LLYHLLJLB (浏览用户浏览记录表)
        user_name = request.session.get('user_name')
        if user_name is None:  #用户未登录(游客身份) 不存储浏览记录
            pass
            #print('游客身份游客身份游客身份游客身份游客身份游客身份游客身份游客身份')
        else:
            lljl = Llyhlljlb(None , id_one , user_name)  #插入记录
            lljl.save()
            #print('插入一个浏览记录插入一个浏览记录插入一个浏览记录插入一个浏览记录插入一个浏览记录插入一个浏览记录插入一个浏览记录插入一个浏览记录')
    except Exception as ex:
        context['info'] = '抱歉! 浏览新闻时出现了异常'
        context['show_state'] = 0 #前端判断为0 弹出一个提示框 告知用户浏览发生异常
        print(ex)
        #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        return render(request , 'show_one_new.html' , context )
    else:
        context['new'] = new
        context['info'] = ''  #新闻获取成功, 向前端显示的异常信息为空
        return render(request, 'show_one_new.html', context)

#按新闻种类展示新闻
def newKind(request , new_kind , pindex):
    #这里 如果new_kind是12 , 最近发布 , 要按时间查询然后排序
    request.session[new_kind] = new_kind  #将新闻类型存在session中 , 当用户点击分页按钮时 , 由showNew来判断改进行什么操作
    request.session['page_count'] = pindex  # 把当前请求的页数存到session里 , 以后用直接取
    if new_kind == "":
        new_kind =1
    else:
        int(new_kind)
    new_list = Xwnrb.objects.filter( fl = new_kind)
    paginator = Paginator(new_list, 5)  # 实例化Paginator, 每页显示5条数据
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    context = {'page': page}
    paginator_count = paginator.count
    print(paginator_count)  #表示 当前查询到的记录的总个数
    if paginator_count == 0:
        context['not_new_message'] = '抱歉! 没有查询到相关的新闻信息哦! '
    src = 'newKind/' + str(new_kind)
    context['urlKind'] = src

    ################################################################
    # releaseNewReturn 变量记录了url的一次状态 , 存储在session中 , 当用户执行发布新闻验证失败后 ,要返回上次浏览的地方 , 这个变量代表上次浏览的位置
    # 他在publisherServer.py 文件的checkPublisher函数中使用 , 相关的变量是url
    # 在本文件的registerInto函数中也用到   对应变量url
    # 在本文件的loginCheck也用到了  对应变量url

    releaseNewReturn = request.get_full_path()
    print(releaseNewReturn)
    request.session['releaseNewReturn'] = releaseNewReturn
    ################################################################

    return render(request, 'hello.html', context)

#搜索完成后 ,点第一页之后的页数走这个函数
def findNew(request ,find_new_pindex):
    txt = request.session.get('findNewTxt')
    new_list = Xwnrb.objects.filter( Q(nr__contains= txt) | Q(bt__startswith = txt) | Q( dy__startswith = txt ) ) #字段名后面加 __contains表示 以txt为所包含的内容来查询
    # __stratswith表示以txt为开头进行查询
    paginator = Paginator(new_list, 5)  # 实例化Paginator, 每页显示5条数据
    page = paginator.page(find_new_pindex)  # 传递当前页的实例对象到前端  搜索时只展示第一页
    request.session['page_count'] = find_new_pindex  # 把当前请求的页数存到session里 , 以后用直接取
    context = {'page': page}
    paginator_count = paginator.count
    print(paginator_count)  # 表示 当前查询到的记录的总个数
    if paginator_count == 0:
        context['not_new_message'] = '抱歉! 没有查询到相关的新闻信息哦! '
    context['urlKind'] = 'findNew'

    ################################################################
    # releaseNewReturn 变量记录了url的一次状态 , 存储在session中 , 当用户执行发布新闻验证失败后 ,要返回上次浏览的地方 , 这个变量代表上次浏览的位置
    # 他在publisherServer.py 文件的checkPublisher函数中使用 , 相关的变量是url
    # 在本文件的registerInto函数中也用到   对应变量url
    # 在本文件的loginCheck也用到了  对应变量url

    releaseNewReturn = request.get_full_path()
    print(releaseNewReturn)
    request.session['releaseNewReturn'] = releaseNewReturn
    ################################################################

    return render(request, 'hello.html', context)

#前端 点击 查找按钮后走这个函数  搜索功能的
def beforeFindNew(request , find_new_pindex):
    txt = request.POST['findNewTxt']
    request.session['findNewTxt'] = txt
    new_list = Xwnrb.objects.filter(
        Q(nr__contains=txt) | Q(bt__startswith=txt) | Q(dy__startswith=txt))  # 字段名后面加 __contains表示 以txt为所包含的内容来查询
    # __stratswith表示以txt为开头进行查询
    paginator = Paginator(new_list, 5)  # 实例化Paginator, 每页显示5条数据
    page = paginator.page(find_new_pindex)  # 传递当前页的实例对象到前端  搜索时只展示第一页
    request.session['page_count'] = find_new_pindex  # 把当前请求的页数存到session里 , 以后用直接取
    context = {'page': page}
    paginator_count = paginator.count
    print(paginator_count)  # 表示 当前查询到的记录的总个数
    if paginator_count == 0:
        context['not_new_message'] = '抱歉! 没有查询到相关的新闻信息哦! '
    context['urlKind'] = 'findNew'

    ################################################################
    # releaseNewReturn 变量记录了url的一次状态 , 存储在session中 , 当用户执行发布新闻验证失败后 ,要返回上次浏览的地方 , 这个变量代表上次浏览的位置
    # 他在publisherServer.py 文件的checkPublisher函数中使用 , 相关的变量是url
    # 在本文件的registerInto函数中也用到   对应变量url
    # 在本文件的loginCheck也用到了  对应变量url

    releaseNewReturn = request.get_full_path()
    print(releaseNewReturn)
    request.session['releaseNewReturn'] = releaseNewReturn
    ################################################################

    return render(request, 'hello.html', context)


#退出
def exitUser(request):
    path_info = request.path_info
    print(path_info)
    print('9999999999999999999999999999999999999999999999999999999999999999999999999999999')
    user_name = request.session.get('user_name')
    context = {}
    if user_name is None:  #用户没有登陆过 ,返回一个无需登陆的信息
        context['exitMessage'] = '您还没有登录 , 无需进行退出操作 !'
    else: #对已经登录的用户信息从session里删除
        del request.session['user_name']
        context['exitMessage'] = '已退出登录'
    return  render(request , 'hello.html' ,context )



