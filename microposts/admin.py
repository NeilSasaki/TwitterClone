from django.contrib import admin

from .models import Post


# 管理画面で表示したいOwnerとContentをlist displayへ設定
class PostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content')


# Postモデルをインポートし、adminへ登録する
admin.site.register(Post, PostAdmin)
