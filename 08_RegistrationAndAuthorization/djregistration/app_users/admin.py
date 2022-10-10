from django.contrib import admin
from app_users.models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_date', 'update_date', 'is_active']
    list_filter = ['create_date', 'tag']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    def get_text(self, object):
        if len(object.text) > 15:
            try:
                return object.text[:15]+'...'
            except:
                return object.text
        else:
            try:
                return object.text[:15]
            except:
                return object.text


    get_text.short_description = 'Описание'
    list_display = ['user_name', 'get_text', 'news_name']
    list_filter = ['user_name']
    actions = ['delete_comment']

    def delete_comment(self, request, queryset):
        queryset.update(text='Удалено администратором')
