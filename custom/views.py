from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

class CustomGet(APIView):
  """
  A custom endpoint for GET request.
  """
  def get(self, request, format=None):
    """
    Return a hardcoded response.
    """
    return Response({"success": True, "content": "Hello World!"})
