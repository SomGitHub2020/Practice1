from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TodoSerializer     
from .models import Todo        
from django_filters.rest_framework import DjangoFilterBackend      

# Create your views here.



class TodoView(viewsets.ModelViewSet):       
    serializer_class = TodoSerializer        
    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']