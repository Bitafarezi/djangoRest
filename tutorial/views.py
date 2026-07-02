from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view()
def hello(request: Request):
    return Response("Hello, world!")


class HelloAPIView(APIView):
    def get(self, request):
        return Response("Hello, world!")
    