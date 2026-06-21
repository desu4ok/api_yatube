from django.contrib import admin
from .models import Comment, Group, Post, Follow  # Добавили Follow в импорт


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_display_links = ('pk', 'text')
    search_fields = ('text', 'author__username')
    list_filter = ('pub_date', 'group')
    readonly_fields = ('pub_date',)
    empty_value_display = '-пусто-'
    ordering = ('-pub_date',)

    def comments_count(self, obj):
        """Подсчёт комментариев к посту"""
        return obj.comments.count()
    comments_count.short_description = 'Кол-во комментариев'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'posts_count')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('posts_count',)

    def posts_count(self, obj):
        """Количество постов в группе"""
        return obj.posts.count()
    posts_count.short_description = 'Кол-во постов'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_preview', 'author', 'post', 'created')
    list_display_links = ('id', 'text_preview')
    search_fields = ('text', 'author__username', 'post__text')
    list_filter = ('created', 'author')
    readonly_fields = ('created',)
    ordering = ('-created',)

    def text_preview(self, obj):
        """Превью текста комментария"""
        if len(obj.text) > 50:
            return obj.text[:50] + '...'
        return obj.text
    text_preview.short_description = 'Комментарий'


# ОБЯЗАТЕЛЬНО ПО ТЗ: Класс управления подписками в админке
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user', 'following')


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)  # Регистрируем подписки