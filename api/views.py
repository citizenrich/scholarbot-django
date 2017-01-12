from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class CustomGet(APIView):
    """
    A custom endpoint for GET request.
    """
    authentication_classes = (TokenAuthentication,JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return a hardcoded response.
        """
        return Response({"success": True, "content": "Hello World!"})
