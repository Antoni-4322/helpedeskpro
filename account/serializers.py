from rest_framework import serializers
from .models import WorkDesk, User

class UserSerializer(serializers.ModelSerializer):
    # work_desk = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['first_name', 'work_desk']
        
        work_desk = serializers.PrimaryKeyRelatedField(
            queryset=WorkDesk.objects.all(),
            many=True,
            
        )
   


