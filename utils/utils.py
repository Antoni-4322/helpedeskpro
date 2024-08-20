#

import threading
import time

from ticket.models import Ticket, Sla, TicketLog
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





def get_display_ticket_type(val):
    ticket_type = Ticket.objects.filter(ticket_type__ticket_type=val)
    return ticket_type

stop_thread = False

def background_task():
    list_updated = []
    while not stop_thread:
        time.sleep(3)
       
        
        list_updated = []
        slas = Sla.objects.filter((Q(status="A") | Q(status="B") | Q(status="C")) & Q(expired=False) ).order_by('status').values()
        
        for sla in slas:
            
            list_origin = list(Ticket.objects.filter(id=sla['ticket_id']).values())
            list_origin[0].update({'status':sla['status'], 'progress':sla['progress']})
            list_updated.append(list(list_origin))

        for ticket in list_updated:

            for ticket_inner in ticket: 
                   
                dt1 = datetime.astimezone(ticket_inner['creation_date']).replace(tzinfo=None)
                dt2 = datetime.now().replace(tzinfo=None)
                td = dt2 - dt1
                minutes = round(timedelta.total_seconds(td) / 60)
               
                initial_minutes = minutes * 100 
                
                final_minutes = int(timedelta.total_seconds(sla_variables[ticket_inner['priority']]) / 60)
                
                cal = round(initial_minutes / final_minutes)
               
                
                if cal > 100:
                    
                    Sla.objects.filter(ticket_id=ticket_inner['id']).update(expired=True, progress=100)
                    modified_fields = {"expired":True}
                    TicketLog.objects.create(log_type=2, user_id=3, ticket_id=ticket_inner['id'], modified_field=modified_fields)
                    
                else:
                    
                    modified_fields = {"expired":False}
                    Sla.objects.filter(ticket_id=ticket_inner['id']).update(progress=cal)

            
      



def check_tickets_on_db():
    
    bg_thread = threading.Thread(target=background_task)
    bg_thread.start()

    # # Somewhere in your main script, when you want to stop the thread:
   
    # bg_thread.join()  # Wait for the thread to finish

        
     

    




    

