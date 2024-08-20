from django.template import Library
from ticket.models import Ticket, Category
from utils import utils
from account.models import WorkDesk, User
from clients.models import Clients

register = Library()

@register.filter
def get_perfil_picture(val):
    image = User.objects.filter(id=val).values('image').first()
    
    return image['image']

@register.filter
def get_display_category(val):
    return Category.objects.filter(id=val).first()

@register.filter
def get_display_user(val):
    return User.objects.filter(id=val).first()


@register.filter
def get_display_work_desk(val):
    return WorkDesk.objects.filter(id=val).first()

@register.filter
def get_display_ticket_type(val):
    ticket_type = Ticket.TICKET_TYPE_CHOICES
    ticket_type_list = dict(ticket_type)
    return ticket_type_list[f'{val}'] 
    
@register.filter
def get_display_priority(val):
    priorities = Ticket.PRIORITY_CHOICES
    priority = dict(priorities)
    return priority[f'{val}']     


@register.filter
def get_display_client(val):
    return Clients.objects.filter(id=val).first()
          