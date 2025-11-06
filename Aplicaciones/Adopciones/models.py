from django.db import models

# Create your models here.
# Persona
class Persona(models.Model):
    id_per = models.AutoField(primary_key=True)
    cedula_per = models.CharField(max_length=20, unique=True)
    nombres_per = models.CharField(max_length=100)
    apellidos_per = models.CharField(max_length=100)
    correo_per = models.EmailField(max_length=100, unique=True)
    telefono_per = models.CharField(max_length=30, blank=True, null=True)
    direccion_per = models.CharField(max_length=200, blank=True, null=True)
    fecha_registro_per = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres_per} {self.apellidos_per}"


#  Mascota
class Mascota(models.Model):
    id_mas = models.AutoField(primary_key=True)
    nombre_mas = models.CharField(max_length=50)
    especie_mas = models.CharField(max_length=50)
    raza_mas = models.CharField(max_length=50, blank=True, null=True)
    sexo_mas = models.CharField(max_length=10, blank=True, null=True)
    edad_anios_mas = models.PositiveIntegerField(default=0)
    estado_mas = models.CharField(max_length=20, default='Disponible')
    fecha_ingreso_mas = models.DateField(auto_now_add=True)
    observaciones_mas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_mas} ({self.especie_mas})"


# Adopción
class Adopcion(models.Model):
    id_ado = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='adopciones')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='adopciones')
    fecha_solicitud_ado = models.DateField(auto_now_add=True)
    fecha_aprobacion_ado = models.DateField(blank=True, null=True)
    estado_ado = models.CharField(max_length=20, default='Solicitada')
    documento_ado = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Adopción #{self.id_ado} - {self.persona.nombres_per} adopta a {self.mascota.nombre_mas}"


