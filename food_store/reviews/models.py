from django.db import models

from users.models import User


class Directory(models.Model):
    """Класс для каталогов."""
    name_catalog = models.CharField(
        max_length=256,
        verbose_name='Каталог',
        unique=True,
        help_text='Укажите название каталога'
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name='Slug',
        unique=True
    )

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'каталог'

    def __str__(self):
        return self.name_catalog


class Categories(models.Model):
    """Класс для под категорий."""
    name_categories = models.CharField(
        max_length=256,
        verbose_name='Категория',
        unique=True,
        help_text='Укажите название категории'
    )
    slug = models.SlugField(
       max_length=256,
       verbose_name='Slug',
       unique=True
    )
    name_catalogs = models.ForeignKey(
        Directory,
        on_delete=models.CASCADE,
        verbose_name='Каталог',
        help_text='Выберите каталог',
        related_name='categories'
    )

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name_categories


class Products(models.Model):
    """Класс для продуктов."""
    name_catalogs = models.ForeignKey(
        Directory,
        on_delete=models.CASCADE,
        verbose_name='Каталог',
        help_text='Выберите каталог',
        # related_name='name_catalogs'
    )
    name_category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Выберите категорию'
        # related_name='name_category'
    )
    name_product = models.CharField(
        max_length=256,
        verbose_name='Наименование товара',
        unique=True,
        help_text='Введите наименование товара'
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name='Slug',
        unique=True
    )
    price = models.FloatField(
        max_length=6,
        verbose_name='Цена за единицу товара',
        help_text='Укажите цену за единицу товара'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='product/',
        help_text='Прикрепите фото товара',
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name_product


class Cart(models.Model):
    """Корзина для пользователей."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='cart')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя: {self.user.username}'


class CartItem(models.Model):
    """Элемент корзины."""
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name='Корзина',
        related_name='items')
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        help_text='Выберите продукт')
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество',
        help_text='Укажите количество товара')

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.product.name_product} в корзине {self.cart.user.username}'
