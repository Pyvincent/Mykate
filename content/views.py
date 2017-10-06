# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from content.models import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def test(request):
    News = u"""
    Weka的全名是怀卡托智能分析环境（Waikato Environment for Knowledge Analysis），是一款免费的，非商业化（与之对应的是SPSS公司商业数据挖掘产品--Clementine ）的，基于JAVA环境下开源的机器学习（machine learning）以及数据挖掘（data mining）软件。它和它的源代码可在其官方网站下载。有趣的是，该软件的缩写WEKA也是New Zealand独有的一种鸟名，而Weka的主要开发者同时恰好来自New Zealand的the University of Waikato。
    """  # 字符串
    Class = ['Chinese', 'English', 'Japanese']  # 列表
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}  # 字典
    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'content/test.html', {'News': News,
                                                  "Class": Class,
                                                  "info_dict": info_dict,
                                                  "List": List})
    # return HttpResponse(u"天王盖地虎，宝塔镇河妖")


def index(request):
    return render(request, 'index.html')


def about_me(reuest):
    return render(reuest, 'aboutme/aboutme.html')


# GET 传入参数的方式计算加法 /add/?a=3&b=4
def add(request):
    a = request.GET.get('a', None)  # a = request.GET['a'] ,b
    b = request.GET.get('b', None)
    c = int(a) + int(b)
    return HttpResponse(str(c))


# url的方式计算加法 /add/a/b/
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))
