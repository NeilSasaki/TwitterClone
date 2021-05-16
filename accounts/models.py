from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    # ユーザー間の多対多の関係を記述
    followers = models.ManyToManyField('self', blank='True', symmetrical='False')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')

    # 　お気に入り機能の追加. Blank Trueを忘れずに。
    # DjangoはデフォルトでManyToManyはUniqueになる。
    # ManyToManyの場合は、on_deleteは不要
    favoritePost = models.ManyToManyField(
        'microposts.Post', blank=True,
        verbose_name='お気に入りの投稿'
    )


class Relationship(models.Model):
    # ここは、user_idではなくuserとすべきだった。。。
    # 自分をフォローしてくれている人
    user_id = models.ForeignKey(Users, related_name='follower', on_delete=models.CASCADE)
    # 自分がフォローしている人
    follow_user_id = models.ForeignKey(Users, related_name='following', on_delete=models.CASCADE)

    # 重複してフォロー関係を作成しなように制約を設定する
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'follow_user_id'],
                                    name='unique-relationship')
        ]

    def __str__(self):
        return "{} : {}".format(self.user_id.username, self.follow_user_id.username)
