from django.urls import path
from .views import inicio, otro_vista, numero_random, numero_del_usuario, mi_plantilla

urlpatterns = [
    path('inicio/', inicio),
    path('', otro_vista),
    path('numero-random/', numero_random),
    path('dame-numero/<numero>', numero_del_usuario),
    # path('dame-numero/<int:numero>', numero_del_usuario),
    path('mi-plantilla/', mi_plantilla),
]
