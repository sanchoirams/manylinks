from django.urls import path

app_name = 'links'

from . import views

urlpatterns = [
    path('novo/', views.add_link, name='add_link'),
    path('lista/', views.lista_links, name='lista'),
    path('apagar/<int:id_link>/', views.apagar_link, name='apagar_link'),
    path('editar/<int:id_link>/', views.editar_link, name='editar_link'),
    path('clique/<int:id_link>/', views.clique_link, name='clique_link'),
]
