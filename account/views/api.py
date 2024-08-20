from django.shortcuts import get_object_or_404, get_list_or_404
from ..models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import UserSerializer
from django.http import HttpResponse
from ticket import models


@api_view()
def user_api_list_work_desk(request, id):

    users = get_list_or_404(
        User.objects.filter(id=id),
        
    )
    
    serializer = UserSerializer(instance=users, many=True)
    
    print(serializer.data)
   
    return Response(serializer.data, status=200)


