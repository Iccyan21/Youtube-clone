from django.contrib.auth.models import AbstractUser,Permission,Group
from django.db import models
from django.conf import settings

class User(AbstractUser):
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='channels_subscribed_to', blank=True),
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='chat_users_permissions', # related_nameを変更
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='accounts_user_groups', # related_nameを変更
        related_query_name='user',
    )