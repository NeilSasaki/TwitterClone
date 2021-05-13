from django.contrib import admin

from django.contrib.auth import get_user_model

# 管理画面で表示したいOwnerとContentをlist displayへ設定
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

#ユーザーモデルを登録する
#get_user_model()で、settings.py ファイルのAUTH_USER_MODELに
# 設定したユーザモデルを呼び出すことができます。
admin.site.register(get_user_model(),UsersAdmin)
