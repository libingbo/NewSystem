# -*- coding: utf-8 -*-

from django.http import HttpResponse
import datetime
from django.db import transaction
from Bean.models import *
from . import NewException
from django.db import connection
from django.db.models.query import QuerySet

class editorXWNRB:
    def __init__(self):
        self.fl = None   #分类
        self.bt = None   #标题
        self.dy = None   #导语
        self.nr = None   #内容
        self.tp = None   #图片
        self.tb = None   #图表
        self.shzt = None #审核状态  false=待审核   true = 已审核
        self.shjg = None #审核结果  false=未通过   true = 已通过
        self.llcs = None #浏览次数
        self.dzcs = None #点赞次数
        self.plcs = None #评论次数
        self.rdz = None  #热度值
        self.fbzyhm = None #发布者用户名
        self.fbsj = None   #发布时间


    def addXWNR_publisher(self , fl , bt , dy , nr , fbzyhm ):  #此处命名和表名不同
        self.fl = fl
        self.bt = bt
        self.dy = dy
        self.nr = nr
        self.tp = None   #只有字符串才可以赋值None
        self.tb = None
        self.shzt = 0  #默认待审核
        self.shjg = 0 #默认未通过
        self.llcs = 0  #数值类型不能赋None
        self.dzcs = 0  #数值类型不能赋None
        self.plcs = 0  #数值类型不能赋None ,可以赋None  ,但是之后加的时候不好做了
        self.rdz = self.llcs * 0.5 + self.dzcs*0.3 + self.plcs*0.2   #数值类型不能赋None
        self.fbzyhm = fbzyhm
        self.fbsj = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     #datatime类型不能赋给值None , 不兼容 ,只能是系统时间
        try:
            with transaction.atomic():
                new = Xwnrb( None, self.fl, self.bt, self.dy, self.nr, self.tp, self.tb, self.shzt, self.shjg, self.llcs, self.dzcs, self.plcs,  self.rdz, self.fbzyhm, self.fbsj)
                #new2 = Xwnrb(None ,2 , '标题3' , '导语3', '内容3' , None ,None , 0 , 0 ,0 , 0 , 0 ,0 , '网三' ,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
                new.save()
        except Exception as ex:
            print("插入新闻时发生错误 , 错误如下:%s" % ex)
            return False
        else:
            return True