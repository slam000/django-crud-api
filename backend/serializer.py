from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Task model.

    This serializer is used to convert Task model instances into JSON
    representation and vice versa. It specifies the fields that should be
    included in the serialized output.

    Attributes:
        model (Task): The Task model class to be serialized.
        fields (str): A string specifying the fields to be included in the
            serialized output. The value '__all__' indicates that all fields
            should be included.

    """
    class Meta:
        model = Task
        fields = '__all__'

