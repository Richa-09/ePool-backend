from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Offer, Request
from django.contrib.auth.models import User
from django.contrib import messages
from .serializers import OfferSerializer, UserSerializer, RequestSerializer


class UserFromTokenViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        user = Token.objects.get(key=request.data['token']).user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        of = Offer()
        of.destination = request.data['destination']
        of.departure = request.data['departure']
        of.date = request.data['date']
        of.time = request.data['time']
        of.seats_available = request.data['seats']
        of.price = request.data['price']
        of.by = request.user
        print(request.user)

        of.save()
        serializer = OfferSerializer(of, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        k = Request()
        k.receiver = request.user
        ride = Offer.objects.get(id=request.data['offer_id'])
        k.provider = ride
        k.pro = ride.by
        k.pickup_location = request.data['pickup_location']
        k.description = request.data['description']
        k.seats_required = request.data['seats_req']
        if k.receiver == k.pro:
            response = messages.error(request, "You can't request your own ride")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        already_exists = Request.objects.all().filter(provider=k.provider).filter(receiver=request.user)
        if len(already_exists) != 0:
            response = messages.error(request, "You have already requested this ride")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if int(k.seats_required) > k.provider.seats_available:
            response = messages.error(request, "No. of seats you requested exceed the limit")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        k.save()
        serializer = RequestSerializer(k, many=False)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

