from rest_framework import serializers

from filemanager.models.file_data import Data

class DataSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    filetype = serializers.SerializerMethodField()
    since_added = serializers.SerializerMethodField()


    class Meta:
        model = Data
        fields = ('file_id', 'file', 'since_added', 'size', 'name', 'filetype')

    def get_size(self, obj):
        file_size = ''
        if obj.file and hasattr(obj.file, 'size'):
            file_size = obj.file.size
        
        return file_size
    
    def get_name(self, obj):
        file_name = ''
        if obj.file and hasattr(obj.file, 'name'):
            file_name = obj.file.name
        
        return file_name
    
    def get_filetype(self, obj):
        file_name = obj.file.name
        
        return file_name.split('.')[-1]
    
    def get_since_added(self, obj):
        date_added = obj.date_created

        return date_added
