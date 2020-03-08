"""newSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add images URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add images URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add images URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.urls import path

from . import view
from . import userEngine
from . import newEngine
from . import a
from . import browserServer
from . import publisherServer

app_name = "news"
urlpatterns = [
    url(r'^testdb$', a.ediuser),
    url(r'^new$' , view.hello),
    path('login/', view.login),  #定位到一个登录界面
    path('loginCheck' , browserServer.loginCheck),  #检查用户登录状态
    path('register' , view.register) , #跳转到注册用户
    path('registerInto', browserServer.registerInto),  # 完成数据库注册用户
    path('hello/<int:pindex>' , browserServer.showNew , name="hello_show"),  #进入首页
    path('oneNew/<int:id_one>' , browserServer.show_one_new ),  #浏览单独一条新闻的请求
    path('intoPublisher' , publisherServer.checkPublisher) ,
    path('joinFamily' , view.joinFamily) , #前端 加入我们  请求
    path('newKind/<int:new_kind>/<int:pindex>' , browserServer.newKind ) ,#带有新闻种类参数的请求  第一个参数是新闻种类, 第二个参数是页数
    path('findNew/<int:find_new_pindex>' , browserServer.findNew) , # 搜索新闻  搜所后, 取第一页之后的数据走这个函数
    path('beforeFindNew/<int:find_new_pindex>' , browserServer.beforeFindNew),#前端点击 搜索 时走这个函数
    path('exitUser'  , browserServer.exitUser) , # 退出
    path('browserConsole' , browserServer.browserConsole) , #浏览者用户进入主页前的检查
    path('browserEditPassword' , browserServer.browserEditPassword) , #浏览者用户重置密码
    path('updateHeadPhoto' , browserServer.updateHeadPhoto) ,   #更新头像
    path('pushHeadPhoto' , browserServer.pushHeadPhoto) #由于传参问题,上传头像的函数处理完成后需要重新刷新到browserConsole.html页面,并带用户头像路径 的参数过去
]
