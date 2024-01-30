from django.urls import path, include
from . import views
# from .views import TodoListView, TodoDetailView, todo_detail, todo_edit, todo_delete
# from .views import TodoListMixins, TodoDetailMixins
# from .views import TodoGenericListView, TodoGenericDetailView
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.TodoListViewSet)


urlpatterns = [
    # path('', views.todo_list),
    # path('detail/<int:pk>', views.todo_detail),
    # path('edit/<int:pk>', views.todo_edit),
    # path('delete/<int:pk>', views.todo_delete),
    # path('list/', TodoListView.as_view()),
    # path('detail/<int:pk>', TodoDetailView.as_view())
    # path('mixin/', TodoListMixins.as_view()),
    # path('mixin/<int:pk>', TodoDetailMixins.as_view()),
    # path('generic/', TodoGenericListView.as_view()),
    # path('generic/<int:pk>/', TodoGenericDetailView.as_view()),
    path('viewset/', include(router.urls)),
]
