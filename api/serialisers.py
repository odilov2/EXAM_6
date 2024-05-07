
from rest_framework import serializers
from music.models import Artist, Albom, Songs
from products.models import Categories, Products, FeaturedProducts
from users.models import Users


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'image')


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('title', 'artist')


class SongsSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)

    class Meta:
        model = Songs
        fields = ('title', 'albom')


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ('title', )


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('title', 'description', 'price')


class FeaturedProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeaturedProducts
        fields = ('title', 'description', 'price')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('first_name', 'last_name')
