from django.conf.urls import url
from . import views
urlpatterns=[
    # #图书对象，GET-->查询所有图书,POST-->添加图书
    url('^books/$',views.BooksView.as_view()),
    # #根据主键指定图书对象，GET-->查询某个图书，PUT-->修改某个图书,DELETE-->删除某个图书
    url(r'^books/(?P<pk>\d+)$',views.BookView.as_view()),
]

# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('book',views.BookViewSet)
# urlpatterns+=router.urls

