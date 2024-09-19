from django import forms
from .models import videojuego , alquiler

class videojuegosForm(forms.ModelForm):
    class Meta:
        model = videojuego
        fields = ['titulo', 'plataforma','genero','stock']

class alquilerForm(forms.ModelForm):
    fecha_alquiler = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    fecha_devolucion = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = alquiler
        fields = ['cliente','videojuego','fecha_alquiler','fecha_devolucion']

