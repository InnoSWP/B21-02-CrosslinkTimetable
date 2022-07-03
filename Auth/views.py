from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import credentials


class AuthAPIView(APIView):
    def post(self, request):
        credentials.login = request.data['login']
        credentials.password = request.data['password']

        return Response({'resp': 200})
