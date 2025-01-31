from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('todos/', ListTodo.as_view(), name='todo-list'),
    path('todos/<int:pk>/', DetailTodo.as_view(), name='todo-detail'),
]