from django.shortcuts import render
from django.http import JsonResponse
from .models import *

#django rest framework decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'LIST':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
