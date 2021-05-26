from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import PostFilter
from .models import Post, User
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class UserList(APIView):
    def get(self, request, username):
        users = User.objects.filter(username=username)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
