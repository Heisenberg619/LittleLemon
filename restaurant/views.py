from django.shortcuts import render
from rest_framework import viewsets,permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer,MenuItemSerializer,BookingSerializer
from .models import MenuItem,Booking

from rest_framework import generics
def index(request):
    return render(request,'index.html',{})

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    permission_classes=[permissions.IsAuthenticated]

class SingleMenuItemsView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    permission_classes=[permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]




