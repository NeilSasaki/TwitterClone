from django.db import models


class Post(models.Model):
    # Postのオーナーを設定する
    owner = models.ForeignKey('accounts.Users', verbose_name='オーナー', on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'


# いいね 機能実装
class Like(models.Model):
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')