from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import *
from .serializers import *

class TownView( APIView ):
    
    def get( self, _, id = None, format=None ):

        if id is not None:
            
            try:
                town = Town.objects.get( id=id )
            except Town.DoesNotExist:
                return Response( status=status.HTTP_404_NOT_FOUND )
            
            serializer = TownSerializer( town )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        municipios = Town.objects.all()
        serializer = TownSerializer( municipios, many=True )
        return Response( serializer.data, status=status.HTTP_200_OK )
    
    def post( self, request, format=None ):
        data = {
            'name': request.data.get('name'),
            'area': request.data.get('area'),
            'budget': request.data.get('budget'),
            'governor': request.data.get('governor'),
        }

        serializer = TownSetSerializer( data = data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete( self, request, id, format = None ):
        try:
            town = Town.objects.get( id=id )
        except Town.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        town.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )

    def put( self, request, id ):
        
        try:
            town = Town.objects.get( id=id )
        except Town.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        data = {
            'name': request.data.get('name'),
            'area': request.data.get('area'),
            'budget': request.data.get('budget'),
            'governor': request.data.get('governor'),
        }
        
        serializer = TownSetSerializer( town, data=data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def patch( self, request, id ):
        
        try:
            person = Town.objects.get( id=id )
        except Town.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        serializer = TownSetSerializer( person, data = request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class TownHousesView( APIView ):
        
    def get( self, _, id = None, format=None ):
        if id is not None:
            houses = House.objects.filter( town=id )
            serializer = BaseHouseSerializer( houses, many=True )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( status=status.HTTP_400_BAD_REQUEST )
        
class HouseView( APIView ):
        
    def get( self, request, id = None, format=None ):
        if id is not None:
            
            try:
                house = House.objects.get( id=id )
            except House.DoesNotExist:
                return Response( status=status.HTTP_404_NOT_FOUND )
    
            serializer = HouseSerializer( house )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        viviendas = House.objects.all()
        serializer = HouseSerializer( viviendas, many=True )
        return Response( serializer.data, status=status.HTTP_200_OK )
    
    def post( self, request, format=None ):
        data = {
            'address': request.data.get('address'),
            'capacity': request.data.get('capacity'),
            'levels': request.data.get('levels'),
            'town': request.data.get('town'),
            'owners' : request.data.get('owners')
        }

        serializer = HouseSetSerializer( data = data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    def delete( self, request, id=None, format=None ):
        print(id)
        try:
            house = House.objects.get( id=id )
        except House.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        house.delete()
        
        #house.save()
        return Response( status=status.HTTP_204_NO_CONTENT )
    
    def put( self, request, id ):
        
        try:
            house = House.objects.get( id=id )
        except House.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        data = {
            'address': request.data.get('address'),
            'capacity': request.data.get('capacity'),
            'levels': request.data.get('levels'),
            'town': request.data.get('town'),
            'owners' : request.data.get('owners')
        }

        serializer = HouseSetSerializer( house, data=data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    def patch( self, request, id ):
        
        try:
            person = House.objects.get( id=id )
        except House.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        serializer = HouseSetSerializer( person, data = request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class HouseResidentsView( APIView ):
            
    def get( self, _, id = None, format=None ):
        if id is not None:
            residentes = Person.objects.filter( home=id )
            serializer = BasePersonSerializer( residentes, many=True )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( status=status.HTTP_400_BAD_REQUEST )

class HouseOwnersView( APIView ):
    
    def get( self, _, id = None, format=None ):
        
        if id is not None:

            try:
                house = House.objects.get( id=id )
            except House.DoesNotExist:
                return Response( status=status.HTTP_404_NOT_FOUND )

            serializer = None

            if house:
                serializer = BasePersonSerializer( house.owners.all(), many=True )
            else:
                serializer = BasePersonSerializer( [], many=True )

            return Response( serializer.data, status=status.HTTP_200_OK )
            
        return Response( status=status.HTTP_400_BAD_REQUEST )

class PersonView( APIView ):
            
    def get( self, _, id = None, format=None ):

        if id is not None:
            
            try:
                person = Person.objects.get( id=id )
            except Person.DoesNotExist:
                return Response( status=status.HTTP_404_NOT_FOUND )
            
            serializer = PersonSerializer( person )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        people = Person.objects.all()
        serializer = PersonSerializer( people, many=True )
        return Response( serializer.data, status=status.HTTP_200_OK )
    
    def post( self, request, format=None ):
        data = {
            'id' : request.data.get('id'),
            'age': request.data.get('age'),
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
            'gender': request.data.get('gender'),
            'home': request.data.get('home'),
            'houses' : request.data.get('houses'),
            'depends_on': request.data.get('depends_on')
        }

        serializer = PersonSetSerializer( data = data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    def delete( self, request, id ):

        try:
            person = Person.objects.get( id=id )
        except Person.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        person.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )
    
    def put( self, request, id ):
        
        try:
            person = Person.objects.get( id=id )
        except Person.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        data = {
            'id' : request.data.get('id'),
            'age': request.data.get('age'),
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
            'gender': request.data.get('gender'),
            'home': request.data.get('home'),
            'depends_on': request.data.get('depends_on'),
            'houses': request.data.get('houses')
        }
        serializer = PersonSetSerializer( person, data=data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def patch( self, request, id ):
        
        try:
            person = Person.objects.get( id=id )
        except Person.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND )
        
        serializer = PersonSetSerializer( person, data = request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class PersonHousesView( APIView ):
            
    def get( self, _, id = None, format=None ):
        if id is not None:

            try:
                person = Person.objects.get( id=id )
            except Person.DoesNotExist:
                return Response( status=status.HTTP_404_NOT_FOUND )
            
            serializer = None

            if person:
                serializer = BaseHouseSerializer( person.houses.all(), many=True )
            else:
                serializer = BaseHouseSerializer( [], many=True )

            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( status=status.HTTP_400_BAD_REQUEST )

class PersonDependencesView( APIView ):
            
    def get( self, _, id = None, format=None ):
        if id is not None:
            dependences = Person.objects.filter( depends_on=id )
            serializer = BasePersonSerializer( dependences, many=True )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( status=status.HTTP_400_BAD_REQUEST )