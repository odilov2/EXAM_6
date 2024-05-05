from rest_framework import serializers

from music.models import Artist, Albom, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'image', 'id')


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('title', 'cover', 'artist')


class SongsSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)

    class Meta:
        model = Songs
        fields = ('title', 'cover', 'albom')
