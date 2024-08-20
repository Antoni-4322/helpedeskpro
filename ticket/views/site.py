from django.shortcuts import render
from ticket.models import Ticket, TicketLog, Sla
from django.views.generic.list import ListView
from django.views import View
from ticket import ticket_forms
from account.models import User
from ticket import models
from clients.models import Clients
import json
from django.db.models import Q
from django.db.models import Count
from datetime import datetime, timedelta
from django.db.models import Sum

from django.db.models import Q
from datetime import datetime, timedelta

SLA_URGENT = datetime.time(datetime(2024, 3, 4, 1, 0, 0))
SLA_URGENT_DELTA = timedelta(0, SLA_URGENT.second, 0, 0, SLA_URGENT.minute, SLA_URGENT.hour, 0)
SLA_HIGHT = datetime.time(datetime(2024, 3, 4, 2, 0, 0))
SLA_HIGHT_DELTA = timedelta(0, SLA_HIGHT.second, 0, 0, SLA_HIGHT.minute, SLA_HIGHT.hour, 0)
SLA_MEDIUM = datetime.time(datetime(2024, 3, 4, 4, 0, 0))
SLA_MEDIUM_DELTA = timedelta(0, SLA_MEDIUM.second, 0, 0, SLA_MEDIUM.minute, SLA_MEDIUM.hour, 0)
SLA_LOW = datetime.time(datetime(2024, 3, 4, 8, 0, 0))
SLA_LOW_DELTA = timedelta(0, SLA_LOW.second, 0, 0, SLA_LOW.minute, SLA_LOW.hour, 0)



sla_variables = {
    'A': SLA_LOW_DELTA,
    'B': SLA_MEDIUM_DELTA,
    'C': SLA_HIGHT_DELTA,
    'D': SLA_URGENT_DELTA
}



def get_clients_organized():
        clients = tuple(Clients.objects.all().values())
        org_list = {}
        delete = []
        new_list = {}
       
        for item in clients:
            item.update({'subs':[]})
            org_list[item['id']] = item
      
        
        new_list = org_list

        for key, values in org_list.items():
            for key_inner, values_inner in list(new_list.items()):
                
                if key == values_inner['sub_id_id']:
                    new_list[key]['subs'].append(values_inner)
                    delete.append(key_inner)
            
                    
        if delete:
            for i in delete:
                del new_list[i]

        return new_list


class Reports(View):
    template_name = 'reports.html'
    def setup(self, *args, **kwargs):
        labels = []
        data = []
        super().setup(*args, **kwargs)
        # labels = ['sao luis', 'sao paulo', 'rio', ' nova york', 'belo horizonte', 'teresina', 'belem']
        # data = [2,5,7,34,6,3,5]

        ##get tickts by category
        by_category = Ticket.objects.values('category__title').order_by('category').annotate(count=Count('category'))
        by_clients = Ticket.objects.values('client_id__name', 'client_id__sub_id__name').order_by('client_id').annotate(count=Count('client_id'))
        by_sub_clients = Ticket.objects.values('client_id__name', 'client_id__sub_id__name')

        

        for ticket in by_clients:
            print(ticket)
            labels.append(  
                str(ticket['client_id__sub_id__name']) + ' > ' + str(ticket['client_id__name'])
            )
            data.append(ticket['count'])

        if self.request.user.is_authenticated:
                self.context = {
                    'labels': labels,
                    'data': data,
                }
                    
        self.rendering = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):        
        return self.rendering

class MyTickets(View):
    template_name = 'my_tickets.html'
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        slas = Sla.objects.filter(Q(status="A") | Q(status="B") |Q(status="C")).order_by('status').values()
        list_updated = []
        for sla in slas:
            list_origin = list(Ticket.objects.filter(id=sla['ticket_id']).values())
            list_origin[0].update({'status':sla['status'], 'progress':sla['progress']})
            list_updated.append(list(list_origin))
            

    
        if self.request.user.is_authenticated:
                self.context = {
                    'slas': list_updated,
                }

        
        self.rendering = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):        
        return self.rendering


class BaseTicket(View):
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        clients = get_clients_organized()
        if kwargs:
            ticket_id = kwargs['id']
            ticket = Ticket.objects.filter(id=ticket_id).first()            
            logs_ticket = TicketLog.objects.filter(ticket_id=ticket_id)

            if self.request.user.is_authenticated:
                self.context = {
                    'forms': ticket_forms.TicketForm(
                        data=self.request.POST or None,
                        user=self.request.user,
                        instance=ticket
                    ),
                    'ticket_id':ticket_id,
                    'logs_ticket':logs_ticket,  
                }
            
        else:
            if self.request.user.is_authenticated:
                self.context = {
                    'forms': ticket_forms.TicketForm(
                        data=self.request.POST or None,
                        user=self.request.user
                    ),
                    'clients': clients 
                }
        self.forms = self.context['forms']
        self.rendering = render(self.request, self.template_name, self.context)

class Add(BaseTicket):
    template_name = 'add.html'
    def get(self, *args, **kwargs):        
        return self.rendering
    def post(self, *args, **kwargs):
        
        if self.forms.is_valid():
            if self.request.user.is_authenticated:
                ...
                self.forms.save()
        else:
           
            return self.rendering
        return self.rendering
    



stop_thread = False

class Edit(BaseTicket):
    template_name = 'edit.html'
    
    def get(self, *args, **kwargs): 
                  
        

        return self.rendering
    
   
    
        
    def post(self, *args, **kwargs):
       
        if self.forms.is_valid():
            if self.request.user.is_authenticated:
                self.forms.save()
        else:
            print("Não é valido")
            return self.rendering
        return self.rendering
    


    
    
    

