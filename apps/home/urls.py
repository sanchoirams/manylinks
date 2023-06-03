from django.urls import path

app_name = 'home'

from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
]
