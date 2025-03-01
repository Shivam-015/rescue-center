import json
from rest_framework import serializers
from  .models import Rescue

class IndexSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rescue
        fields='__all__'

    def validate_facilities(self,value):
        if isinstance(value, bytes): 
            value = value.decode("utf-8", errors="ignore")
        if isinstance(value,str):               #isinstance is used to convert string into list form
            try:
                value = json.loads(value)       # convert string into list
                if not isinstance(value,list):
                    raise serializers.ValidationError(" ")
            except json.JSONDecodeError:    #jsondecodeerror is used to display error 
                raise serializers.ValidationError("Facilities must be a valid JSON array")
        return value


    def validate_form_12a(self,value):
        try:
           
            if value.size> 5 * 1024 *1024:
                raise serializers.ValidationError("file size should be 5Mb")
            if not value.name.endswith(('.pdf','.docx','.doc')):
                raise serializers.ValidationError("only PDF and doc files are allowed")
            return value
        except UnicodeDecodeError:
            raise serializers.ValidationError("Invalid file encoding. Please upload a UTF-8 encoded file.")
        

    def validate_form_13a(self,value):
        return self.validate_form_12a(value)





