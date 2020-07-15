from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TodoSerializer     
from .models import Todo        
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os 
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

class TodoView(viewsets.ModelViewSet):       
    serializer_class = TodoSerializer        
    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']


class ReactAppView(View):

    def get(self, request):
        try:

            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )