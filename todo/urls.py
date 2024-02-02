from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.TodoListViewSet)


urlpatterns = [
    # path('', views.todo_list),
    # path('detail/<int:pk>', views.todo_detail),
    # path('edit/<int:pk>', views.todo_edit),
    # path('delete/<int:pk>', views.todo_delete),
    # path('list/', views.TodoListView.as_view()),
    # path('detail/<int:pk>', views.TodoDetailView.as_view())
    path('mixin/', views.TodoListMixins.as_view()),
    path('mixin/<int:pk>', views.TodoDetailMixins.as_view()),
    path('generic/', views.TodoGenericListView.as_view()),
    path('generic/<int:pk>/', views.TodoGenericDetailView.as_view()),
    path('viewset/', include(router.urls)),
    path('user/', views.UserGenericView.as_view()),
]
