from rest_framework import serializers
from . models import Category, Ticket
from account.models import WorkDesk, User

class TicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Ticket
        fields = '__all__'

        id = serializers.IntegerField()
        subject = serializers.CharField()
        description = serializers.CharField(max_length=255)
        client_id = serializers.CharField()
        
        work_desk_id = serializers.PrimaryKeyRelatedField(
            queryset=WorkDesk.objects.all()
        )
        my_user = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
            source='user'
        )
        united_fields = serializers.SerializerMethodField()

        category = serializers.PrimaryKeyRelatedField(
            queryset=Category.objects.all(),
        )

        # def get_united_fields(self, ticket):
        #     return f'{ticket.ticket_type}, {ticket.status}'
    

