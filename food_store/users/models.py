from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField(
        max_length=256,
        unique=True,
        verbose_name='e-mail',
        help_text='Укажите свой e-mail'
    )
    username = models.CharField(
        max_length=256,
        verbose_name='Никнем пользователя',
        help_text='Укажите свой никнем',
        unique=True,
        validators=[
            RegexValidator(
                r'^[\w.@+-]+\Z',
                'Поле username содержит недопутимые символы.'
            )
        ]

    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
