from django.db import models

class Municipio( models.Model ):

    class Meta:
        db_table = "MUNICIPIO"
    
    id = models.BigAutoField( primary_key=True )
    nombre = models.CharField( max_length=45 )
    area = models.DecimalField( max_digits=10, decimal_places=2 )
    presupuesto = models.DecimalField( max_digits=10, decimal_places=2 )

    gobernador = models.OneToOneField(
        'Persona',
        on_delete=models.CASCADE,
    )

class Vivienda( models.Model ):

    class Meta:
        db_table = "VIVIENDA"

    id = models.BigAutoField( primary_key=True )
    direccion = models.CharField( max_length=45 )
    capacidad = models.IntegerField()
    niveles = models.IntegerField()
    municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE
    )

class Persona( models.Model ):

    class Meta:
        db_table = "PERSONA"

    class SexoChoises( models.TextChoices ):
        MASCULINO = 'M', 'Masculino'
        FEMENINO = 'F', 'Femenino'
        OTRO = 'O', 'Otro'

    id = models.BigAutoField( primary_key=True )
    edad = models.IntegerField()
    nombre = models.CharField( max_length=45 )
    telefono = models.CharField( max_length=20 )
    sexo = models.CharField( 
        max_length=1,
        choices=SexoChoises.choices,
        default=SexoChoises.OTRO
    )
    
    hogar = models.ForeignKey(
        Vivienda,
        on_delete=models.CASCADE
    )

