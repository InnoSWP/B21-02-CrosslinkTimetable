from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class AuthAPIView(APIView):
    def get(self, request):


        return Response({'resp': 200})
