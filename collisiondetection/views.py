from django.shortcuts import render
from rest_framework import viewsets, generics , status
from rest_framework.response import Response
from .models import ObstacleDetectionEvent
from .serializers import ObstacleDetectionEventSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from hardware_project_main.asgi import notify_clients_about_message



class ObstacleDetectionEventViewSet(generics.GenericAPIView):
    queryset = ObstacleDetectionEvent.objects.all()
    serializer_class = ObstacleDetectionEventSerializer

    def post(self, request, *args, **kwargs):
        timestamp = request.data.get('timestamp')
        description = request.data.get('description')
        image = request.data.get('image')
        
        data_to_save = {'timestamp': timestamp, 'description': description}

        # Create a serializer instance with the data
        serializer = self.get_serializer(data=data_to_save)
        
        # Validate and save the data to the database
        if serializer.is_valid():
            serializer.save()
            saved_id = serializer.instance.id
            print("the id is", saved_id)
            notify_clients_about_message(timestamp, description, saved_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request, *args, **kwargs):
        specific_id = kwargs.get('id')

        if specific_id is not None:
            # Retrieve the specific object based on the provided ID
            try:
                obj = ObstacleDetectionEvent.objects.get(id=specific_id)
                serialized_data = ObstacleDetectionEventSerializer(obj).data
                serialized_data['id'] = obj.id
                return Response(serialized_data)
            except ObstacleDetectionEvent.DoesNotExist:
                return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
            
        else:

        # Retrieve all objects from the database
            queryset = ObstacleDetectionEvent.objects.all()
            # queryset = self.get_queryset()
            
            # Serialize the data
            # serializer = self.get_serializer(queryset, many=True)

            serialized_data = []
            for obj in queryset:
                data = ObstacleDetectionEventSerializer(obj).data
                data['id'] = obj.id
                serialized_data.append(data)
            # Return the serialized data in the response
            return Response(serialized_data)

