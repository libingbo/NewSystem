# -*- coding: utf-8 -*-

from django.http import HttpResponse
import datetime
from django.db import transaction
from Bean.models import *
from . import NewException


# 数据库操作
def testdb(request):
    test1 = Xwfbyhb(yhm='张三' , mm='123' , qx='111111' , sr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), xb='男' , gxqm='美好生活每一天' , tx=None)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

#它针对新闻发布用户表的3种操作 添加 删除 更新
#其中 , 删除方法为发布者和管理员两个角色共有
#添加方法 , addXWFBYH_admin由管理员角色调用   addXWFBYH_publisher由发布者角色调用
#更新方法 , ediXWFBYH_admin由管理员角色调用   addXEFBYH_publisher由发布者角色调用
class editorXWFBYHB:
    def __init__(self):
        self.yhm = None
        self.mm = None
        self.qx = None
        self.sr = None
        self.xb = None
        self.gxqm = None
        self.tx = None

    #添加新闻发布者
    # 有默认值的参数放最后
    # 注意这里的构造方法参数位置 , 以为有默认值的放在了最后 , 所以传参的时候参数位置也要对应改变
    #该方法由新闻管理者调用
    def addXWFBYH_admin(self ,  yhm ,mm ,xb ,gxqm ,tx , qx='111111' ,sr=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):  #注意这里命名时没有B , 和表名不同
        self.yhm = yhm
        self.mm = mm
        self.qx = qx
        self.sr = sr
        self.xb = xb
        self.gxqm = gxqm
        self.tx = tx

        try:
            user = Xwfbyhb( None ,  self.yhm , self.mm , self.qx , self.sr , self.xb , self.gxqm , self.tx)
            if(self.xb in ['男' , '女']):
                user.save()
            else:
                raise NewException.XBException
        except NewException.XBException as xbex:
            print("出现了如下异常(性别值异常)%s" % xbex.message)
            return False
        except Exception as ex:
            print("出现如下异常%s" % ex)
            return False
        else:
            return True

        # 添加新闻发布者
        # 有默认值的参数放最后
        # 注意这里的构造方法参数位置 , 以为有默认值的放在了最后 , 所以传参的时候参数位置也要对应改变
        # 该方法由新闻发布者调用
        def addXWFBYH_publisher(self, yhm, mm, xb, gxqm, tx, sr=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):  # 注意这里命名时没有B , 和表名不同
            self.yhm = yhm
            self.mm = mm
            self.qx = '111111'  #创建用户时给默认权限111111
            self.sr = sr
            self.xb = xb
            self.gxqm = gxqm
            self.tx = tx

            try:
                user = Xwfbyhb(None, self.yhm, self.mm, self.qx, self.sr, self.xb, self.gxqm, self.tx)
                if (self.xb in ['男', '女']):
                    user.save()
                else:
                    raise NewException.XBException
            except NewException.XBException as xbex:
                print("出现了如下异常(性别值异常)%s" % xbex.message)
                return False
            except Exception as ex:
                print("出现如下异常%s" % ex)
                return False
            else:
                return True




    #删除新闻发布者
    #按 用户名(yhm) 索引来删除发布者
    def delXWFBYH(self , yhm_out):
        try:
            with transaction.atomic():
                user = Xwfbyhb.objects.get(yhm = yhm_out)
                user.delete()
        except Exception as ex:
            print("删除数据出现错误:%s" % ex)
            return False
        else:
            return True


    #编辑新闻发布者
    #该方法由新闻发布者调用
    #新闻发布者不能更改自己的权限
    def ediXWFBYH_publisher(self ,yhm_edi ,mm ,xb ,gxqm ,tx ,sr=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ):
        #这里还没有判断性别 , 前端是一个多选框 , 只能选男和女 ,先不用写 , 表里xb列没有check约束
        try:
            with transaction.atomic():
                user = Xwfbyhb.objects.get(yhm = yhm_edi)
                user.yhm = yhm_edi
                user.mm = mm
                user.xb = xb
                user.gxqm = gxqm
                user.tx = tx
                user.sr= sr
                user.save()
        except Exception as ex:
            print("编辑用户信息出错:%s" % ex)
            return False
        else:
            return True


    #编辑新闻发布者
    #该方法有新闻管理者调用
    #新闻管理者只能更改新闻发布者的权限字段
    def ediXWFBYH_admin(self , yhm_edi , qx_edi):
        try:
            with transaction.atomic():
                user = Xwfbyhb.objects.get(yhm = yhm_edi)
                user.qx = qx_edi
                user.save()
        except Exception as ex:
            print("管理员编辑新闻发布者权限出错 ,定位: userEngine.ediXWFBYH_admin-----:%s" % ex)
            return False
        else:
            return True


#它针对新闻浏览用户表的三种操作  添加 , 更改 ,删除
#其中 ,删除操作为 浏览者和管理者共用
#添加操作仅浏览者使用
#更改操作 , 管理者角色使用ediXWLLYH_admin  浏览者角色使用ediXWLLYH_browser
class editorXWLLYHB:
    def __init__(self):
        self.yhm = None
        self.mm = None
        self.qx = None
        self.sr = None
        self.xb = None
        self.gxqm = None
        self.tx = None

    #添加新闻浏览表记录
    #由新闻浏览者角色调用
    def addXWLLYH_browser(self , yhm, mm, xb, gxqm, tx, sr=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ):
        self.yhm = yhm
        self.mm = mm
        self.xb = xb
        self.gxqm =gxqm
        self.tx = tx
        self.sr = sr
        self.qx = '111111'  #默认创建浏览者时的权限为111111

        try:
            user = Xwllyhb(None, self.yhm, self.mm, self.qx, self.sr, self.xb, self.gxqm, self.tx)
            if (self.xb in ['男', '女']):
                user.save()
            else:
                raise NewException.XBException
        except NewException.XBException as xbex:
            print("出现了如下异常(性别值异常)%s" % xbex.message)
            return False
        except Exception as ex:
            print("出现如下异常%s" % ex)
            return False
        else:
            return True

    # 删除新闻浏览者
    # 按 用户名(yhm) 索引来删除浏览者
    def delXWLLYH(self, yhm_out):
        try:
            with transaction.atomic():
                user = Xwllyhb.objects.get(yhm=yhm_out)
                user.delete()
        except Exception as ex:
            print("删除数据出现错误:%s" % ex)
            return False
        else:
            return True


    #编辑新闻浏览者记录
    #由管理员角色调用, 只能编辑权限字段
    def ediXWLLYH_admin(self , yhm_edi , qx_edi):
        try:
            with transaction.atomic():
                user = Xwllyhb.objects.get(yhm=yhm_edi)
                user.qx = qx_edi
                user.save()
        except Exception as ex:
            print("管理员编辑新闻浏览者权限出错 ,定位: userEngine.ediXWLLYH_admin-----:%s" % ex)
            return False
        else:
            return True

    #编辑新闻浏览者记录
    #由新闻浏览者角色调用  不能编辑权限字段
    def ediXWLLYH_browser(self ,yhm_edi , mm, xb, gxqm, tx, sr=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ):
        # 这里还没有判断性别 , 前端是一个多选框 , 只能选男和女 ,先不用写 , 表里xb列没有check约束
        try:
            with transaction.atomic():
                user = Xwllyhb.objects.get(yhm=yhm_edi)
                user.yhm = yhm_edi
                user.mm = mm
                user.xb = xb
                user.gxqm = gxqm
                user.tx = tx
                user.sr = sr
                user.save()
        except Exception as ex:
            print("编辑用户信息出错:%s" % ex)
            return False
        else:
            return True

    #新闻浏览用户重置密码时调用
    #执行修改密码操作的前提是用户已经登录, 而登录阶段已经检查过密码的正确性 , 所以这里不再检查旧密码是否正确
    def editXWLLYH_Password(self ,request ,  oldMm , newMm):
        user_name = request.session.get('user_name')
        try:
            user = Xwllyhb.objects.get(yhm=user_name)
            user.mm = newMm
            return True
        except:
            return False



class editorXWGLYHB:
    def __init__(self):
        self.xm = None  #姓名
        self.sr = None  #生日
        self.gh = None  #工号
        self.lxfs = None #联系方式
        self.xb = None   #性别

        #这个表没有密码字段 , 先等一下
