from rest_framework import serializers
from  .models import AnimalRescueRequest

class IndexSerializers(serializers.ModelSerializer):
    class Meta:
        model=AnimalRescueRequest
        fields='__all__'