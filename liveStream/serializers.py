from rest_framework import serializers
from liveStream.models import ArtistModel,FileModel


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = ['title','created_on','artist_name']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['song','upload_file']