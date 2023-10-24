from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Note    ## renders the data from the database model
from .serializers import NoteSerializer
from notes_api import serializers
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote

# Create your views here.


## This view is going to specify all the routes inside the app ##
@api_view(['GET'])
def get_routes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    
    return Response(routes)

@api_view(['GET', 'POST'])
def getNotes(request):
    
    if request.method == 'GET':
        return getNotesList(request)
    
        
    if request.method == 'POST':
        return createNote(request)
    

@api_view(['GET', 'PUT', 'DELETE'])    
def getNote(request, pk):
    
    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)
        
    if request.method == "DELETE":
        return deleteNote(request, pk)
        


## Making RESTful API ##
"""
/notes GET
/notes POST
/notes/<id> GET
/notes/<id> PUT
/notes/<id> DELETE

"""

"""
## API to render the data(multiple notes or all notes) from the database ##

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-update')  ## get all the notes from database
    serializer = NoteSerializer(notes, many = True )  #many specifies to serialize multiple objects
    return Response(serializer.data)

## API to render the data(single notes) from the database ##

@api_view(['GET'])
def getNote(request, pk): #primary key is passed
    note = Note.objects.get(id=pk)  ## get all the notes from database
    serializer = NoteSerializer(note, many = False )  #many specifies to serialize multiple objects
    return Response(serializer.data)

## API to create a Note
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many= False)
    return Response(serializer.data)
    
## API to update the notes
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data # takes the fetch request from the frontend
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

## API to delete the note
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk).delete()
    return Response('Note was deleted!')

"""