from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import *
from .serializers import *

class MunicipioView( APIView ):
    
    def get( self, _, id = None, format=None ):

        if id is not None:
            municipio = Town.objects.get( id=id )
            serializer = TownSerializer( municipio )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        municipios = Town.objects.all()
        serializer = TownSerializer( municipios, many=True )
        return Response( serializer.data, status=status.HTTP_200_OK )
    
    def post( self, request, format=None ):
        data = {
            'name': request.data.get('name'),
            'area': request.data.get('area'),
            'budget': request.data.get('budget'),
        }

        serializer = TownSerializer( data = data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete( self, id ):
        municipio = Town.objects.get( id=id )
        municipio.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )

    def put( self, request, id ):
        municipio = Town.objects.get( id=id )
        data = {
            'name': request.data.get('name'),
            'area': request.data.get('area'),
            'budget': request.data.get('budget'),
        }
        serializer = TownSerializer( municipio, data=data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class ViviendaView( APIView ):
        
    def get( self, _, id = None, format=None ):

        if id is not None:
            vivienda = House.objects.get( id=id )
            serializer = HouseSerializer( vivienda )
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
        }

        serializer = BaseHouseSerializer( data = data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    def delete( self, id ):
        vivienda = House.objects.get( id=id )
        vivienda.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )
    
    def put( self, request, id ):
        vivienda = House.objects.get( id=id )
        data = {
            'address': request.data.get('address'),
            'capacity': request.data.get('capacity'),
            'levels': request.data.get('levels'),
            'town': request.data.get('town'),
        }
        serializer = BaseHouseSerializer( vivienda, data=data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class PersonaView( APIView ):
            
    def get( self, _, id = None, format=None ):

        if id is not None:
            persona = Person.objects.get( id=id )
            serializer = PersonSerializer( persona )
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        personas = Person.objects.all()
        serializer = PersonSerializer( personas, many=True )
        return Response( serializer.data, status=status.HTTP_200_OK )
    
    def post( self, request, format=None ):
        data = {
            'id' : request.data.get('id'),
            'age': request.data.get('age'),
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
            'gender': request.data.get('gender'),
            'home': request.data.get('home'),
            'depends_on': request.data.get('depends_on'),
        }

        serializer = PersonSerializer( data = data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    def delete( self, id ):
        persona = Person.objects.get( id=id )
        persona.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )
    
    def put( self, request, id ):
        persona = Person.objects.get( id=id )
        data = {
            'id' : request.data.get('id'),
            'age': request.data.get('age'),
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
            'gender': request.data.get('gender'),
            'home': request.data.get('home'),
            'depends_on': request.data.get('depends_on'),
        }
        serializer = PersonSerializer( persona, data=data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )
        
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
