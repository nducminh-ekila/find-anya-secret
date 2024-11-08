from django.urls import path
from .views.pages import index
from .views.users import user_create, user_list
from .views.user_sessions import user_login, user_logout

urlpatterns = [
    path('', index, name='index'),
    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('user_sessions/create/', user_login, name='user_session_create'),
    path('user_sessions/destroy/', user_logout, name='user_session_destroy'),
]
