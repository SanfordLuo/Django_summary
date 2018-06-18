from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def hello(request):
    return HttpResponse("hello friday")

# 模板应用
def index1(request):
    # 1.获取模板
    template = loader.get_template('index.html')
    context = {'friday': '不能说的秘密'}

    # 2.渲染模板
    return HttpResponse(template.render(context))

def index2(request):
    context = {'friday': 'secret'}
    return render(request, 'index.html', context)

def index3(request):
    context = {
        'name': 'jayChou',
        'my_dict': {
            'first': '蒲公英的约定',
            'second': '七里香'
        },
        'my_list': [1, 2, 3, 4]
    }
    return render(request, 'index3.html', context)