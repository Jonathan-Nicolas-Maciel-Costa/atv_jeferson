from django.urls import path, include
from .api.viewset import AlbumViewSet
urlpatterns = [
    path('list_albuns', AlbumViewSet.as_view(), name="teste"),

]
