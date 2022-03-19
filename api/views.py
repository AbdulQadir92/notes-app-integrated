from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import *
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

## REST / RESTFUL API with utils.py to clean up code ##
@api_view(['GET', 'POST'])
def getNotes(request):

    if request.method == 'GET':
        return getNotesList(request)

    if request.method == 'POST':
        return createNote(request)

    
@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetails(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)



#     ## REST / RESTFUL API without utils.py ##
# @api_view(['GET', 'POST'])
# def getNotes(request):

#     if request.method == 'GET':
#         notes = Note.objects.all().order_by('-updated')
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         data = request.data
#         note = Note.objects.create(
#             body=data['body']
#         )
#         serializer = NoteSerializer(note, many=False)
#         return Response(serializer.data)

    
# @api_view(['GET', 'PUT', 'DELETE'])
# def getNote(request, pk):

#     if request.method == 'GET':
#         note = Note.objects.get(id=pk)
#         serializer = NoteSerializer(note, many=False)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         data = request.data
#         note = Note.objects.get(id=pk)
#         serializer = NoteSerializer(instance=note, data=data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         note = Note.objects.get(id=pk)
#         note.delete()
#         return Response('Note was deleted')




    ## API ##
# @api_view(['GET'])
# def getNotes(request):
#     notes = Note.objects.all().order_by('-updated')
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)    

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)    

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted')