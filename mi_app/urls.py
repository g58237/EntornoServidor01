from django.urls import path
'computación en la nube'
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('tecnologias/', views.tecnologias, name='tecnologias'),
]