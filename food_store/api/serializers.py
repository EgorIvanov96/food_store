from rest_framework import serializers

from users.models import User
from reviews.models import Directory, Categories, Products, Cart, CartItem


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    name_catalog = serializers.CharField(source='name_catalogs.name_catalog')

    class Meta:
        model = Categories
        fields = ('name_categories', 'slug', 'name_catalog')


class ProductsSerializer(serializers.ModelSerializer):
    name_catalogs = serializers.CharField()
    name_category = serializers.CharField()

    class Meta:
        model = Products
        fields = '__all__'


class DirectorySerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Directory
        fields = ('id', 'name_catalog', 'slug', 'categories')


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, required=False)
    total_price = serializers.SerializerMethodField()
    total_items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price', 'total_items']
        read_only_fields = ['user', 'total_price', 'total_items']

    def get_total_price(self, obj):
        return sum(item.total_price() for item in obj.items.all())

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        cart = Cart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])
        instance.save()

        # Обновляем существующие или создаем новые элементы корзины
        for item_data in items_data:
            item_id = item_data.get('id')
            if item_id:
                item = CartItem.objects.get(id=item_id, cart=instance)
                item.quantity = item_data.get('quantity', item.quantity)
                item.save()
            else:
                CartItem.objects.create(cart=instance, **item_data)

        return instance
