from django.db import models

class Town( models.Model ):

    class Meta:
        db_table = "TOWN"
    
    id = models.BigAutoField( primary_key=True )
    name = models.CharField( max_length=45 )
    area = models.DecimalField( max_digits=10, decimal_places=2 )
    budget = models.DecimalField( max_digits=10, decimal_places=2 )

    governor = models.OneToOneField(
        'Person',
        related_name = 'governed_town',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

class House( models.Model ):

    class Meta:
        db_table = "HOUSE"

    id = models.BigAutoField( primary_key=True )
    address = models.CharField( max_length=45 )
    capacity = models.IntegerField()
    levels = models.IntegerField()
    town = models.ForeignKey(
        Town,
        related_name='houses',
        on_delete=models.CASCADE,
        null = False, blank = False
    )

class Person( models.Model ):

    class Meta:
        db_table = "PERSON"

    class SexoChoises( models.TextChoices ):
        MASCULINO = 'M', 'Masculino'
        FEMENINO = 'F', 'Femenino'
        OTRO = 'O', 'Otro'

    id = models.IntegerField( primary_key=True )
    age = models.IntegerField()
    name = models.CharField( max_length=45 )
    phone = models.CharField( max_length=20 )
    gender = models.CharField( 
        max_length=1,
        choices=SexoChoises.choices,
        default=SexoChoises.OTRO
    )
    
    home = models.ForeignKey(
        House,
        related_name='residents',
        on_delete=models.CASCADE,
        null = True, blank = True
    )

    depends_on = models.ForeignKey(
        'self', related_name='dependences',
        on_delete=models.CASCADE,
        null = True, blank = True
    )

    houses = models.ManyToManyField(
        House, related_name='owners'
    )

