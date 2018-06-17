import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def index(request):
    return HttpResponse('hello django')

# 反解析
def index2(request):
    url_str = reverse('userss:indexx')
    return HttpResponse(url_str)
    # http://127.0.0.1:8000/users/index2

# 在路由中提取参数
def show(request, a, b):
    return HttpResponse("%s---%s" % (a, b))

# 查询地址中的字符串
# http://127.0.0.1:8000/users/get1?a=1&a=2&c=python
def get1(request):
    dict1 = request.GET
    # print(type(dict1))    # <class 'django.http.request.QueryDict'>
    a = dict1.getlist('a')
    b = dict1.get('b')
    c = dict1.get('c')
    return HttpResponse('%s---%s---%s' % (a, b, c))

# 请求体参数：表单
def post1(request):
    dict2 = request.POST
    a = dict2.getlist('a')
    b = dict2.get('b')
    c = dict2.get('c')
    return HttpResponse('%s---%s---%s' % (a, b, c))

# 请求体参数：非表单，现在通用json格式数据:put-raw-json
def put1(request):
    json_data = request.body.decode()
    dict3 = json.loads(json_data)
    return HttpResponse("ook")

# 响应对象，返回json数据
def json(request):
    return JsonResponse({'a':10,'b':'hello'})