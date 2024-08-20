
from django.db import models
from clients.models import Clients
from account.models import WorkDesk, User
from rest_framework import serializers

import json

class TesteDb(models.Model):
    teste = models.CharField(max_length=2, null=True)


class TicketLog(models.Model):

    log_type = models.PositiveIntegerField(null=True)
    datetime_log = models.DateTimeField(auto_now_add=True, null=True)
    user_id = models.PositiveIntegerField()
    ticket_id = models.PositiveIntegerField(null=True)
    modified_field = models.JSONField(null=True)

class Category(models.Model):
        parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)        
        title = models.CharField(max_length=100, null=True)
        def __str__(self):                           
            full_path = [self.title]                  
            k = self.parent
            while k is not None:
                full_path.append(k.title)
                k = k.parent
            return ' -> '.join(full_path[::-1])  

class Sla(models.Model):

    STATUS_CHOICES = (
            ('A', 'Em Espera'),
            ('B', 'Atendendo'),
            ('C', 'Pausado'),
            ('D', 'Concluido'),
    )


    expired = models.BooleanField(default=False)

    ticket_id = models.PositiveIntegerField(null=True)
    status = models.CharField(
        max_length=2,
        default='A',
        choices=STATUS_CHOICES
    )
    progress = models.PositiveIntegerField(default=0)

    
class Ticket(models.Model):
    PRIORITY_CHOICES = (
            ('A', 'Baixa'),
            ('B', 'Media'),
            ('C', 'Alta'),
            ('D', 'Urgente'),
    )

    TICKET_TYPE_CHOICES = (
            ('A', 'Incidente'),
            ('B', 'Problema'),
            ('C', 'Requisição'),
    )


   
    subject = models.CharField(max_length=200, null=True, verbose_name="Assunto")
    description = models.CharField(max_length=300, null=True, verbose_name="Descrição")
    client_id = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    comments = models.TextField(blank=True)
    work_desk_id = models.ForeignKey(WorkDesk, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    ticket_type = models.CharField(
        max_length=2,
        default='A',
        choices=TICKET_TYPE_CHOICES
    )

    priority = models.CharField(
        max_length=2,
        default='A',
        choices=PRIORITY_CHOICES
        
    )

   

    def __str__(self) -> str:
        return f'{self.subject}'
    
    def save(self):
        super().save()
        data = self
        
        serializer = TicketSerializer(instance=self, many=False)
        json_data = json.dumps(serializer.data)
        user_id = self.user.id
        ticket_id = self.id
        json_converted = json.loads(json_data)
        
        TicketLog.objects.create(log_type=1, user_id=user_id, ticket_id=ticket_id, modified_field=json_converted)
        Sla.objects.create(ticket_id=ticket_id)

class TickerSerializerString(serializers.ModelSerializer):
     ticket_type = serializers.StringRelatedField()
     class Meta:
        model = Ticket
        fields = '__all__'
         


class TicketSerializer(serializers.ModelSerializer):
     class Meta:
          model = Ticket
          fields = '__all__'
         
