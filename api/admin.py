from django.contrib import admin

from api.models import Header, SlideMain, IconMain, FeedbackPost, Product, Services, Feedback, StaticText


# Register your models here.
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'year']
    search_fields = ['name', 'email', 'phone_number']


class SlideMainAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['page_data']


class IconMainAdmin(admin.ModelAdmin):
    list_display = ['id', 'header_logo']
    search_fields = ['page_data']
    list_filter = ['page_data']


@admin.register(FeedbackPost)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'text')


@admin.register(StaticText)
class StaticTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'Is_Active')
    list_filter = ('Is_Active',)
    search_fields = ('text',)


# Регистрируем модели и классы администратора
admin.site.register(Header, HeaderAdmin)
admin.site.register(SlideMain, SlideMainAdmin)
admin.site.register(IconMain, IconMainAdmin)
