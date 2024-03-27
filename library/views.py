from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book
from .serlizers import Books_Detail_Serlizers, Books_Serlizers
# Create your views here.

class AddBookView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=Books_Detail_Serlizers
    
class ListBookView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=Books_Serlizers

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=Books_Detail_Serlizers
    lookup_field='ISBN'
    

