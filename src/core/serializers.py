from rest_framework import serializers
from .models import *

class BaseHouseSerializer( serializers.ModelSerializer ):
    class Meta:
        model = House
        fields = ('id', 'address', 'capacity', 'levels', 'town')

class BaseTownSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Town
        fields = ('id', 'name', 'area', 'budget', 'governor')

class BasePersonSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Person
        fields = ('id', 'name', 'gender', 'age', 'phone', 'home')

class HouseSetSerializer( BaseHouseSerializer ):
    owners = serializers.ListField(
        child = serializers.IntegerField(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = House
        fields = '__all__'

    def create( self, validated_data ):
        owners = validated_data.pop( 'owners', [])
        
        house = House.objects.create( **validated_data )

        if owners is not None:
            house.owners.set( owners )

        return house

    def update( self, instance, validated_data ):
        owners = validated_data.pop( 'owners', [])
        if owners is not None:
            instance.owners.set( owners )

        super().update( instance, validated_data )
        return instance

class HouseSerializer( BaseHouseSerializer ):
    town = BaseTownSerializer( many=False, read_only=True )
    residents = BasePersonSerializer( many=True, read_only=True )
    owners = BasePersonSerializer( many=True, read_only=True )
    
    class Meta:
        model = House
        fields = '__all__'

class TownSerializer( BaseTownSerializer ):
    houses = BaseHouseSerializer( 
        many=True, read_only=True 
    )
    governor = BasePersonSerializer( 
        many=False, read_only=True 
    )

    class Meta:
        model = Town
        fields = '__all__'

class TownSetSerializer( serializers.ModelSerializer ):
    governor = serializers.IntegerField(
        write_only=True,
        required=False,
        allow_null=True
    )
    houses = serializers.ListField(
        child = serializers.IntegerField(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Town
        fields = '__all__'

    def create( self, validated_data ):
        governor_id = validated_data.pop( 'governor', None)
        houses = validated_data.pop( 'houses', [])
        town = Town.objects.create( **validated_data )

        if governor_id is not None:
            try:
                governor_person = Person.objects.get( id=governor_id )
                town.governor = governor_person
            except Person.DoesNotExist:
                pass
        else:
            town.governor = None
        
        houses_objs = [ House.objects.get( id=house_id ) for house_id in houses ]

        # Reassign array of houses (old ones will remain around here)
        town.houses.set( houses_objs )
        return town

    def update( self, instance, validated_data ):
        governor_id = validated_data.pop( 'governor', None)
        houses = validated_data.pop( 'houses', [])

        if governor_id is not None:
            try:
                governor_person = Person.objects.get( id=governor_id )
                instance.governor = governor_person
            except Person.DoesNotExist:
                pass
        else:
            instance.governor = None
        
        houses_objs = [ House.objects.get( id=house_id ) for house_id in houses ]

        # Reassign array of houses (old ones will remain around here)
        instance.houses.set( houses_objs )

        super().update( instance, validated_data )
        return instance

class PersonSerializer( BasePersonSerializer ):
    houses = BaseHouseSerializer( many=True, read_only=True )
    dependences = BasePersonSerializer( many=True, read_only=True )
    depends_on = BasePersonSerializer( many=False, read_only=True )
    home = BaseHouseSerializer( many=False, read_only=True )
    governed_town = BaseTownSerializer( many=False, read_only=True )

    class Meta:
        model = Person
        fields = '__all__'

class PersonSetSerializer( serializers.ModelSerializer ):
    houses = serializers.ListField(
        child = serializers.IntegerField(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Person
        fields = '__all__'

    def create( self, validated_data ):
        houses = validated_data.pop( 'houses', [])
        
        person = Person.objects.create( **validated_data )

        if houses is not None:
            person.houses.set( houses )

        return person

    def update( self, instance, validated_data ):
        houses = validated_data.pop( 'houses', [])

        if houses is not None:
            instance.houses.set( houses )

        return super().update( instance, validated_data )