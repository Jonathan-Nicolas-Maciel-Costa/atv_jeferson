from rest_framework import serializers
from ..models import Album

class AlbumSerializers (serializers.Serializer):

    class Meta:
        
        model = Album
        fields = '__all__'
        