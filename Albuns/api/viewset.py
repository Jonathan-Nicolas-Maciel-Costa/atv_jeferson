from rest_framework import serializers, viewsets
from .serialisers import AlbumSerializers
from ..models import Album
class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class  = AlbumSerializers
