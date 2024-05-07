from music.models import Songs, Albom, Artist
from products.models import Categories, Products, FeaturedProducts
from users.models import Users
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serialisers import (ArtistSerializer, AlbomSerializer, SongsSerializer, CategoriesSerializer, ProductsSerializer,
                          FeaturedProductsSerializer, UsersSerializer)

from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    pagination_class = LimitOffsetPagination


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=title', ]
    pagination_class = LimitOffsetPagination

class SongAPIViewSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['=title', ]
    pagination_class = LimitOffsetPagination

class CategoryAPIViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['=title', ]
    pagination_class = LimitOffsetPagination

class ProductsAPIViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['=title', 'price']
    pagination_class = LimitOffsetPagination


class FeaturedProductsAPIViewSet(ModelViewSet):
    queryset = FeaturedProducts.objects.all()
    serializer_class = FeaturedProductsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['=title', 'price']
    pagination_class = LimitOffsetPagination


class UsersAPIViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['=first_name', ]
    pagination_class = LimitOffsetPagination

