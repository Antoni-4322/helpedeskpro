from django import forms
from django.forms import Textarea
from . import models
import json
from .serializers import TicketSerializer



class TicketForm(forms.ModelForm):

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = models.Ticket
        fields = '__all__'
        
        exclude = ('comments',)
        widgets = {
            'description': Textarea(),
        }

        

        

    def clean(self, *args, **kwargs):
        # data = self.data
        # cleaned = self.cleaned_data
        # json_data = json.dumps(data)
        # user_id = self.user.id
        # ticket_id = self.ticket_id
        # models.Ticket.objects.create(1, user_id, json_data)
        
        if self.user:
            ...