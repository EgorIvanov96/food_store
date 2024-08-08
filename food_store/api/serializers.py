from rest_framework import serializers

from users.models import User
from reviews.models import Directory, Categories, Products


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
