from django.urls import path
from .views import inicio, otro_vista, numero_random, numero_del_usuario, mi_plantilla, login, registrar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('otra-vista/', otro_vista, name="otra_vista"),
    path('numero-random/', numero_random, name="numero_random"),
    path('dame-numero/<numero>/', numero_del_usuario, name="numero_del_usuario"),
    # path('dame-numero/<int:numero>', numero_del_usuario),
    path('mi-plantilla/', mi_plantilla, name="mi_plantilla"),
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('logout/', LogoutView.as_view(template_name='indice/logout.html'), name='logout'),
]
