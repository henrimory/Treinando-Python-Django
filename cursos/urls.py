from django.urls import path
from.import views

urlpatterns = [
    path('acessar_curso/' , views.acessar_curso),
    path('criar_curso/' , views.criar_curso),
    path('listar_curso/' , views.listar_curso)
]