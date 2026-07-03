from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

@api_view()
def hello(request: Request):
    return Response("Hello, world!")


class HelloAPIView(APIView):
    def get(self, request):
        return Response("Hello, world!")
    

class BookDetailAPIView(APIView):
    
    # Read/Retrieve All (GET) -> Get list of all books
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = BookSerializer(book)               # many=True for .all()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # Create (POST) -> Create a new book
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        
        return Response({"message": "book deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)
        