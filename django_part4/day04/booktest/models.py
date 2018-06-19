from django.db import models

# Create your models here.

# 定义图书模型类BookInfo
class BookInfo(models.Model):
    # 书名
    title = models.CharField(max_length=20, verbose_name='书名')
    # 发布日期
    pub_date = models.DateField(verbose_name='日期')
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    comment = models.IntegerField(default=0)
    # 逻辑删除
    is_delete = models.BooleanField(default=False)
    # 保存到:media_root/booktest/文件名
    face = models.ImageField(upload_to='booktest', verbose_name='封面', null=True,blank=True)

    # 自定义表信息,Meta是固定的
    class Meta:
        # 定义表名
        db_table = 'tb_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def bpub_date(self):
        return self.pub_date.strftime('%Y-%m-%d')

    bpub_date.short_description = '自定义日期'
    bpub_date.admin_order_field = 'id'


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    # 姓名
    name = models.CharField(max_length=10)
    # 性别:男male==0，女female==1
    gender = models.BooleanField(default=False)
    # 简介
    content = models.CharField(max_length=200)
    # 逻辑删除
    is_delete = models.BooleanField(default=False)
    # 外键：参数为类的名称
    book = models.ForeignKey('BookInfo')
    #隐含属性：book_id
    #book代表一个BookInfo类型的对象
    #book_id代表某个对象的主键值

    class Meta:
        verbose_name = '英雄'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
    #
    def book_title(self):
        # [id]title
        return '[%d]%s' % (self.book.id, self.book.title)