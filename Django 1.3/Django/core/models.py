from django.db import models


# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column="idgenero", primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(
        "Genero", on_delete=models.CASCADE, db_column="idgenero"
    )
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellido_paterno)
            + " "
            + str(self.apellido_materno)
        )



class Tour(models.Model):
    id_tour = models.AutoField(db_column="idtour", primary_key=True)
    nombre_tour = models.CharField(max_length=20)
    tipo_tour = models.CharField(max_length=20)
    fecha_de_tour = models.DateField(blank=False, null=False)
    precio = models.IntegerField()
    cantidad_personas = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='tours/', blank=True, null=True)

    def __str__(self):
        return str(self.nombre_tour) + " " + str(self.tipo_tour) + " " + str(self.id_tour)

class CarritoItem(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)  # Añade un valor por defecto aquí

    def __str__(self):
        return f"{self.figura.nombre_figura} - {self.cantidad}"
