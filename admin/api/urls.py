from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    # Logins, Registrations, Logout API endpoints
    path('register/', Register.as_view(), name='register'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Features API endpoints
    path('', ListTodo.as_view(), name='todo'),
    path('todo/<int:pk>/', DetailTodo.as_view(), name='todo-detail'),
    path('todo/create/', CreateTask.as_view(), name='todo-create'),
    path('todo/update/<int:pk>/', UpdateTask.as_view(), name='todo-update'),
    path('todo/delete/<int:pk>/', DeleteTodo.as_view(), name='todo-delete'),
]