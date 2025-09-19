from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fotos, name='lista_fotos'),
    path('<int:foto_id>/', views.detalhe_foto, name='detalhe_foto'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('', views.lista_fotos, name='home'),
]
