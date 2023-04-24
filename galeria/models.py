from django.db import models

# Create your models here.


class Fotografia(models.Model):
    """docstring for Fotografia."""
    
    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=True, blank=True)
    categoria = models.CharField(max_length=100, default='', choices=OPCOES_CATEGORIA)
    descricao = models.TextField(null=True, blank=True)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"

    