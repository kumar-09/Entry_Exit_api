from django.shortcuts import render
from django.http import JsonResponse
from .models import guest, Event_DB, userEvent
from .serializers import guestSerializer, Event_DBSerializer, userEventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def event_list(request, format=None):

    if request.method == 'GET':
        events = Event_DB.objects.all()
        serializer = Event_DBSerializer(events, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Event_DBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, event_id, format=None):
    try:
        event = Event_DB.objects.get(pk=event_id)
    except Event_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Event_DB
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Event_DBSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def guest_list(request, format=None):

    if request.method == 'GET':
        guests = guest.objects.all()
        serializer = guestSerializer(guests, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = guestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def guest_detail(request, userid, format=None):
    try:
        event = guest.objects.get(pk=userid)
    except guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = guest
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = guestSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
