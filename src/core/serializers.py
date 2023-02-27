from rest_framework import serializers
from .models import *

class BaseHouseSerializer( serializers.ModelSerializer ):
    class Meta:
        model = House
        fields = '__all__'

class BaseTownSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Town
        fields = '__all__'

class BasePersonSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Person
        fields = '__all__'

class HouseSerializer( BaseHouseSerializer ):
    town = BaseHouseSerializer( many=False, read_only=True )
    residents = BasePersonSerializer( many=True, read_only=True )
    owners = BasePersonSerializer( many=True, read_only=True )
    
    class Meta:
        model = House
        fields = '__all__'

class TownSerializer( BaseTownSerializer ):
    houses = BaseHouseSerializer( many=True, read_only=True )
    governor = BasePersonSerializer( many=False, read_only=True )

    class Meta:
        model = Town
        fields = '__all__'

class PersonSerializer( BasePersonSerializer ):
    houses = BaseHouseSerializer( many=True, read_only=True )
    dependences = BasePersonSerializer( many=True, read_only=True )
    dependiente = BasePersonSerializer( many=False, read_only=True )
    hogar = BaseHouseSerializer( many=False, read_only=True )
    municipio_gobernado = BaseTownSerializer( many=False, read_only=True )

    class Meta:
        model = Person
        fields = '__all__'
