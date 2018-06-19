from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

# Register your models here.

# 调整站点显示信息
admin.site.site_header = '以飞书屋'
admin.site.site_title = '以飞书屋MIS'
admin.site.index_title = '欢迎使用以飞书屋MIS'

# 定义嵌入类
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 1

# 定制类
class BookInfoAdmin(admin.ModelAdmin):
    # 列表页选项
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True
    list_display = ['id', 'title', 'pub_date', 'bpub_date', 'face']

    # 编辑页选项
    # fields=['title','pub_date']

    fieldsets = (
        ('必填项', {'fields': ('title', 'pub_date')}),
        ('可填项', {'fields': ('bread', 'comment', 'face')}),
    )

    #添加嵌入类
    # inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'book_title']
    list_filter = ['book', 'gender']  # 右侧快速过滤
    search_fields = ['name', 'content']  # 顶部搜索框

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
