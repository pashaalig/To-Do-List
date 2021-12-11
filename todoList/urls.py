from django.urls import path
from todoList.views import *

urlpatterns = [
    path('', home, name='home'),
    # path('task/', task, name='task'),
    path('login/', login_user, name='login_user'),
    path('logout/',logout_user, name='logout_user'),
    path('signup/', signup_user, name='signup_user'),
    path('add/', add_todo, name='add_todo'),
    path('delete-todo/<int:id>', delete_todo, name='delete_todo'),
    path('edit-todo/<int:id>', edit_todo, name='edit_todo'),
]