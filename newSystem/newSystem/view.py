from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def fbuser(request):
    return render(request, 'publisherConsole.html')

#将 login 请求跳转到login.html
def login(request):
    return render(request , 'login.html')

#将 register 请求定位到 register.html
def register(request):
    return render(request , 'register.html')

#前端 加入我们  功能 , 跳转到joinFamily.html 公司介绍页面
def joinFamily(request):
    return render(request , 'joinFamily.html')