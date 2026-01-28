from django import forms
from .models import Comentario_Producto
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario_Producto
        fields = ['mensaje']  # o ['texto', 'calificacion'] si tu modelo tiene rating
        labels = {
            'mensaje': 'Comentario',
        }
        widgets = {
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }