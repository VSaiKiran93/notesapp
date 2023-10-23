from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note    ## renders the data from the database model
from .serializers import NoteSerializer

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


## API to render the data(multiple notes or all notes) from the database ##

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()  ## get all the notes from database
    serializer = NoteSerializer(notes, many = True )  #many specifies to serialize multiple objects
    return Response(serializer.data)

## API to render the data(single notes) from the database ##

@api_view(['GET'])
def getNote(request, pk): #primary key is passed
    note = Note.objects.get(id=pk)  ## get all the notes from database
    serializer = NoteSerializer(note, many = False )  #many specifies to serialize multiple objects
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