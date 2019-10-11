from rest_framework import viewsets
from filemanager.models.file_data import Data
from filemanager.serializers.file_serializers import DataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer