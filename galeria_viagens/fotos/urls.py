from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fotos, name='lista_fotos'),
    path('<int:foto_id>/', views.detalhe_foto, name='detalhe_foto'),
]
