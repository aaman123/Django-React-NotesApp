from .models import Note
from .serializers import NoteSerializer

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
  return Response("Our API")

@api_view(['GET'])
def getHealth(request):
  return Response("Everything is A Ok", status.HTTP_200_OK)

@api_view(['GET'])
def getNotes(request):
  notes = Note.objects.all()
  serializer = NoteSerializer(notes, many = True)

  return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
  notes = Note.objects.get(id=pk)
  serializer = NoteSerializer(notes, many = False)

  return Response(serializer.data)

@api_view(['POST'])
def postNote(request):

  if request.method == 'POST':
    serializer = NoteSerializer(data = request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status= status.HTTP_201_CREATED)

    return Response(serializer.data, status.HTTP_400_BAD_REQUEST)