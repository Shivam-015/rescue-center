from rest_framework import status
from rest_framework.views import APIView   #apiview= class based view  or handles the request like get or post
from rest_framework.response import Response  #response = jo hume user ko print karana h 
from .models import AnimalRescueRequest
from .serializers import IndexSerializers
from rest_framework.parsers import MultiPartParser, FormParser   #multipartparser is used to handle file uploads means to store files pdf or videos # formparser is used to accept or store form data means text




class userData(APIView):    # handles request
    def get(self, request):  #request=get  database to user
        documents=AnimalRescueRequest.objects.all()   #objects = ek puri row...     all = sara data of table which are in our row
        serializer=IndexSerializers(documents,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class uploadview(APIView):  #POST METHOD
    parser_classes =(MultiPartParser,FormParser)

    def post(self, request):
        variableHu = request.data.dict()  # Convert QueryDict to dict

       
        serializer = IndexSerializers(data=variableHu)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully!"}, status=status.HTTP_201_CREATED)

        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



    def get(self,request):  #request=get  database to user
        documents=AnimalRescueRequest.objects.all()   #objects = ek puri row...     all = sara data of table which are in our row
        serializer=IndexSerializers(documents,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

