from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class BusquedaCurso(forms.Form):
    partial_curso = forms.CharField(label='Buscador',max_length=20)