from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'authorization'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page='articles:index'), name='logout'),
    path('register/', views.register, name='register'),
]
