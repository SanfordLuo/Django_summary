from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from . import decorators
# Create your views here.
from django.views import View


def cookie_set(request):
    response = HttpResponse('ok')
    response.set_cookie('name1', 'sanford')
    response.set_cookie('name2', 'jay', max_age=3600)
    return response

def cookie_get(request):
    name1 = request.COOKIES.get('name1')
    return HttpResponse(name1)

def session_set(request):
    request.session['name3'] = 'Luo'
    request.session.set_expiry(3600)
    return HttpResponse('okkkk')

def session_get(request):
    you_name = request.session.get('name3')
    return HttpResponse(you_name)

# 视图函数上添加装饰器
# @decorators.register
def show(request):
    print('----view')
    # return HttpResponse("使用装饰器")
    return HttpResponse("使用中间件")


# 类视图
@method_decorator(decorators.register, name='dispatch')
class RegisterView(View):
    # @decorators.register
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')
