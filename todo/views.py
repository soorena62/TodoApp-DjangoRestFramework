from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, mixins
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer, UserTodoSerializer
from .models import Todo


# Create your views here:


User = get_user_model()


class UserGenericView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserTodoSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# Generic Base Views Start

class TodoGenericListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TodoGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# Mixin Base Views Start:

class TodoListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodoDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk: int):
        return self.update(request, pk)

    def delete(self, request: Request, pk: int):
        return self.destroy(request, pk)


# Class Base Views Start:

# class TodoListView(APIView):
#     def get_list(self, request: Request):
#         todos_queryset = Todo.objects.order_by('priority').all()
#         todos_serializer = TodoSerializer(todos_queryset, many=True)
#         return Response(todos_serializer.data, status=status.HTTP_200_OK)
#
#     def post_list(self, request: Request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(None, status.HTTP_400_BAD_REQUEST)
#
#
# class TodoDetailView(APIView):
#     def get_object(self, pk: int):
#         try:
#             todo: Todo = Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             return Response(None, status.HTTP_404_NOT_FOUND)
#
#     def get_view(self, request, pk):
#         todo = self.get_object(pk=pk)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         todo = self.get_object(pk=pk)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, "Content Edited")
#         return Response(None, status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         todo = self.get_object(pk)
#         todo.delete()
#         return Response(None, "Content Deleted!")


#  Functional Base Views Start:

# @api_view(['GET', 'POST'])
# def todo_list(request: Request):
#     if request.method == 'GET':
#         todos_queryset = Todo.objects.order_by('priority').all()
#         todos_serializer = TodoSerializer(todos_queryset, many=True)
#         return Response(todos_serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     return Response(None, status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def todo_detail(request: Request, pk):
#     try:
#         todo: Todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(None, status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#
# @api_view(['PUT'])
# def todo_edit(request: Request, pk):
#     try:
#         todo: Todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(None, status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, "Content Edited")
#         return Response(None, status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['DELETE'])
# def todo_delete(request: Request, pk):
#     try:
#         todo: Todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(None, status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#         todo.delete()
#         return Response(None, "Content Deleted!")
