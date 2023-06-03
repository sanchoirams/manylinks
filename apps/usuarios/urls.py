from django.urls import path

app_name = 'usuarios'

from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('novo/', views.add_usuario, name='add_usuario'),
]
