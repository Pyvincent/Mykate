from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    News = """
    Weka的全名是怀卡托智能分析环境（Waikato Environment for Knowledge Analysis），是一款免费的，非商业化（与之对应的是SPSS公司商业数据挖掘产品--Clementine ）的，基于JAVA环境下开源的机器学习（machine learning）以及数据挖掘（data mining）软件。它和它的源代码可在其官方网站下载。有趣的是，该软件的缩写WEKA也是New Zealand独有的一种鸟名，而Weka的主要开发者同时恰好来自New Zealand的the University of Waikato。
    """  # 字符串
    Class = ['Chinese', 'English', 'Japanese']  # 列表
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}  # 字典
    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'content/index.html', {'News': News,
                                                  "Class": Class,
                                                  "info_dict": info_dict,
                                                  "List": List})
    # return HttpResponse(u"天王盖地虎，宝塔镇河妖")


# GET 传入参数的方式计算加法 /add/?a=3&b=4
def add(request):
    a = request.GET.get('a', 0)  # a = request.GET['a'] ,b
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


# url的方式计算加法 /add/a/b/
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))


def login(reuest):
    return render(reuest, 'content/login.html')