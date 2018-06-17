from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),

    # 反解析用
    url(r'^index2$', views.index2, name='indexx'),

    # 路由中提取参数用
    url(r'^show/(\d+)/(\d+)$',views.show), # 第一个参数给a,第二个参数化给b

    # 查询地址中的字符串
    url(r'^get1$', views.get1),

    # 请求体参数：表单
    url(r'^post1', views.post1),

    # 请求体参数：非表单，现在通用json格式数据:put-raw-json
    url(r'put1', views.put1),

    # 响应对象，返回json数据
    url(r'json', views.json),

]
