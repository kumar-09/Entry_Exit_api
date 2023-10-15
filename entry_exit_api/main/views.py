from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Guests, Event_DB, userEvent, GeneratedPrime
from .serializers import GuestsSerializer, Event_DBSerializer, userEventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import qrcode
import sympy
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


@api_view(['GET', 'POST'])
def guest_list(request, format=None):

    if request.method == 'GET':
        guests = Guests.objects.all()
        serializer = GuestsSerializer(guests, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GuestsSerializer(data=request.data)
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
        serializer = Event_DBSerializer(event)
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


@api_view(['GET', 'PUT', 'DELETE'])
def guest_detail(request, userid, format=None):
    try:
        guest = Guests.objects.get(pk=userid)
    except Guests.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestsSerializer(guest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GuestsSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def userevent_list(request, format=None):

    if request.method == 'GET':
        userevs = userEvent.objects.all()
        serializer = userEventSerializer(userevs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = userEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def userEvent_detail(request, event_id, format=None):
    try:
        userevent = userEvent.objects.get(pk=event_id)
    except userEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = userEventSerializer(userevent)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = userEventSerializer(userevent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userevent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def generate_prime(request):
    # Generate a new prime number
    prime1 = sympy.randprime(10, 1000)
    prime2 = sympy.randprime(10000, 15000)
    generated_prime = GeneratedPrime(value=prime1*prime2)
    generated_prime.save()

    # Create a QR code with the prime number
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(prime1*prime2))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Serve the QR code image as an HTTP response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
