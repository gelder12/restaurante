from django.db import models
from django.contrib import admin

#Define la clase Menu, esta tabla no se relaciona con nadie más.
class Menu(models.Model):
    nombre  =   models.CharField(max_length=30)
    tipoproducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

#En un misma cliente ordena varios menus, y un menu puede ser ordenado por varios cleintes.
#Por lo tanto necesitamos una relación many to many (muchos a muchos).
#Aquí indicamos que la propiedad menus es del tipo Many to Many.
# Y le indicamos que se relaciona con Menu a través (through) la clase Orden, que se define más adelante.
class Cliente(models.Model):
    nombre    = models.CharField(max_length=60)
    fecha_orden = models.DateField()
    edad      = models.IntegerField()
    direccion = models.CharField(max_length=100)
    nit       = models.IntegerField()
    clientes   = models.ManyToManyField(Menu, through='Orden')
    def __str__(self):
        return self.nombre

#Definimos la clase intermedia que se encargará de relacionar de uno a muchos Cliente y Menu.
#En esta definimos las llaves foraneas que nos relacionan a Menu y a Cliente.
# on_delete = models.CASCADE le indica que en caso de eliminar borre en cascada los datos relacionados.
class Orden (models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

#Estas clases las usamos para indicarle a la página admin que despliegue los datos relacionados en linea.
#Es decir en el mismo formulario ambas tablas.
class OrdenInLine(admin.TabularInline):
    model = Orden
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = (OrdenInLine,)

class ClienteAdmin (admin.ModelAdmin):
    inlines = (OrdenInLine,)
