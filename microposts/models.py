from django.db import models


class Post(models.Model):
    # Postのオーナーを設定する
    owner = models.ForeignKey('accounts.Users', verbose_name='オーナー', on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.content
