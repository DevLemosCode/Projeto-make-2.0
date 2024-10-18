from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_item, name='registrar_item'),
    path('', views.listar_estoque, name='listar_estoque'),
]
