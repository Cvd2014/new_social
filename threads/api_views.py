from rest_framework import generics
from models import Subject, Thread,Post
from serializers import ThreadSerializer, PostSerializer

class ThreadViewSet(generics.ListAPIView):
    queryset=Thread.objects.all()
    serializer_class = ThreadSerializer