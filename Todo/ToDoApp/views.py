from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)


class TodosListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JWTAuthentication,)


class TodosRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'An error occurred.'}, status=500)


class TodosUpdateAPIView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'An error occurred.'}, status=500)


class TodosDestroyAPIViewView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'An error occurred.'}, status=500)


class TodosListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        try:
            todos = self.get_queryset()
            serialized_todos = self.serializer_class(todos, many=True)
            return render(request, 'ToDoApp/todos_list.html', {'todos': serialized_todos.data})
        except Exception:
            return Response({'error': 'An error occurred.'}, status=500)

