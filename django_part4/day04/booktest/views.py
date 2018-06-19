import json
from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from .models import BookInfo
from django.views import View


class BooksView(View):
    def get(self, request):
        '''
        查询所有图书对象
        '''
        blist = BookInfo.objects.all()  # [book,book,...]
        # 将列表对象转成列表，里面存字典
        blist2 = []
        for book in blist:
            book_dict = {
                'id': book.id,
                'title': book.title,
                'pub_date': book.pub_date.strftime('%Y-%m-%d')
            }
            blist2.append(book_dict)
        return JsonResponse({'blist': blist2})  # {blist:[{},{},{}...]}

    def post(self, request):
        '''
        添加图书对象
        '''
        # 接收
        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)
        # 创建对象并保存
        title1 = json_dict.get('title')
        pub_date1 = datetime.strptime(json_dict.get('pub_date'), '%Y-%m-%d')
        book = BookInfo.objects.create(title=title1, pub_date=pub_date1)
        # 返回
        return JsonResponse({
            'id': book.id,
            'title': book.title,
            'pub_date': book.pub_date.strftime('%Y-%m-%d')
        })


class BookView(View):
    def get(self, request, pk):
        '''
        根据主键查询图书对象
        '''
        book = BookInfo.objects.get(pk=pk)
        return JsonResponse({
            'id': book.id,
            'title': book.title,
            'pub_date': book.pub_date.strftime('%Y-%m-%d')
        })

    def put(self, request, pk):
        '''
        根据主键修改图书对象
        '''
        # 接收
        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)
        # 修改并保存
        book = BookInfo.objects.get(pk=pk)
        book.title = json_dict.get('title')
        book.pub_date = datetime.strptime(json_dict.get('pub_date'), '%Y-%m-%d')
        book.save()
        # 返回
        return JsonResponse({
            'id': book.id,
            'title': book.title,
            'pub_date': book.pub_date.strftime('%Y-%m-%d')
        })

    def delete(self, request, pk):
        '''
        根据主键删除图书对象
        '''
        book = BookInfo.objects.get(pk=pk)
        book.delete()
        return HttpResponse(status=204)
