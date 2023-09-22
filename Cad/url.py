from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import 



urlpatterns = [path('', IndexView.as_view(), name='index'),
               path('create/usuario', CreateUsuario.as_view(), name='createusuario'),
               path('create/cargo', CreateCargo.as_view(), name='createcargo'),
               path('update/usuario/<int:pk>', UpdateUsuario.as_view(), name='updateusuario'),
               path('update/cargo/<int:pk>', UpdateCargo.as_view(), name='updatecargo'),
               path('delete/usuario/<int:pk>', DeleteUsuario.as_view(), name='deleteusuario'),
               path('delete/cargo/<int:pk>', DeleteCargo.as_view(), name='deletecargo'),
               path('list/usuario', ListUsuario.as_view(), name='listusuario'),
               path('list/cargo', ListCargo.as_view(), name='listcargo'),
               path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
               path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
               ]