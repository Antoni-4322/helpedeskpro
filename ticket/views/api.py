from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import TicketSerializer
from ..models import Ticket, TicketLog
from django.shortcuts import get_list_or_404, get_object_or_404


@api_view()
def ticket_api_list(request):
    tickets = get_list_or_404(
        Ticket.objects.order_by("-id"),
    )
    serializer = TicketSerializer(instance=tickets, many=True)
    return Response(serializer.data)


@api_view()
def ticket_api_detail(request, id):
    tickets = get_object_or_404(
        Ticket,
        id=id
    )
    serializer = TicketSerializer(instance=tickets, many=False)
    return Response(serializer.data)



def ticket_edit(request):
    values = request.GET
    ticket_id = values['ticket_id']
    attribute_name = values['attribute_name']
    item_value = values['item_value']
    user_id = request.user.id


    
    if attribute_name == 'category':
        
        json_converted = {'category':item_value}
        
        Ticket.objects.filter(id=ticket_id).update(category=item_value)
        TicketLog.objects.create(log_type=2, user_id=user_id, ticket_id=ticket_id, modified_field=json_converted)
    if attribute_name == 'work_desk_id':
        Ticket.objects.filter(id=ticket_id).update(work_desk_id=item_value)
    if attribute_name == 'user':
        
        Ticket.objects.filter(id=ticket_id).update(user=item_value)
    
    if attribute_name == 'ticket_type':
        Ticket.objects.filter(id=ticket_id).update(ticket_type=item_value)
    
    if attribute_name == 'priority':
        Ticket.objects.filter(id=ticket_id).update(priority=item_value)
    if attribute_name == 'status':
        Ticket.objects.filter(id=ticket_id).update(status=item_value)

    
    data = {'ola'}
   
    return HttpResponse(data)