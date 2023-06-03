from django.urls import path

app_name = 'links'

from . import views

urlpatterns = [
    path('novo/', views.add_link, name='add_link'),
]
