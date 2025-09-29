from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Reto(models.Model):
    DIFICULTAD_CHOICES = [
        ('F', 'Fácil'),
        ('M', 'Medio'),
        ('D', 'Difícil'),
    ]
    
    TIPO_CHOICES = [
        ('M', 'Matemático'),
        ('L', 'Lógico'),
        ('S', 'Sudoku'),
        ('P', 'Problema'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    contenido = models.TextField() 
    dificultad = models.CharField(max_length=1, choices=DIFICULTAD_CHOICES)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    respuesta_correcta = models.CharField(max_length=200)
    puntos = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo

class Alternativa(models.Model):
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE, related_name='alternativas')
    texto = models.CharField(max_length=200)
    es_correcta = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.reto.titulo} - {self.texto}"

class IntentoReto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200)
    es_correcto = models.BooleanField()
    fecha_intento = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['usuario', 'reto'] 
    
    def __str__(self):
        return f"{self.usuario.username} - {self.reto.titulo}"

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos_totales = models.IntegerField(default=0)
    retos_resueltos = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"