from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on Task objects.

    Inherits from viewsets.ModelViewSet, which provides default implementations for
    the standard CRUD actions (list, create, retrieve, update, partial_update, destroy).

    Attributes:
        queryset (QuerySet): The queryset of Task objects to be used by the viewset.
        serializer_class (Serializer): The serializer class to be used for Task objects.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    