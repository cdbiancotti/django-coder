from django.urls import path
# from .views import nuevo_curso, formulario_curso, busqueda_curso, listado_estudiantes
from . import views


urlpatterns = [
    path('nuevo/', views.nuevo_curso, name='nuevo_curso'),
    path('curso/', views.formulario_curso, name='formulario_curso'),
    path('busqueda-curso/', views.busqueda_curso, name="busqueda_curso"),
    
    path('estudiante/listado/', views.listado_estudiantes, name="listado_estudiantes"),
    # path('estudiante/', estudiante, name="estudiante"),
    path('estudiante/crear/', views.crear_estudiante, name="crear_estudiante"),
    path('estudiante/borrar/<int:id>/', views.borrar_estudiante, name="borrar_estudiante"),
    path('estudiante/actualizar/<int:id>/', views.actualizar_estudiante, name="actualizar_estudiante"),
    
    path('profesores/', views.ProfesorLista.as_view(), name="profesor_listado"),
    # path('profesores/<int:pk>', views.ProfesorDetalle.as_view(), name="profesor_detalle")
    path("profesores/<int:pk>/", views.ProfesorDetalle.as_view(), name="profesor_detalle"),
    path("profesores/<int:pk>/editar/", views.ProfesorEditar.as_view(), name="profesor_editar"),
    path("profesores/<int:pk>/borrar/", views.ProfesorBorrar.as_view(), name="profesor_borrar")

]
