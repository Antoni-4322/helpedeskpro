from django.contrib import admin
from . models import Ticket, Category, TicketLog, TesteDb, Sla


class TicketAdmin(admin.ModelAdmin):
    list_display = 'subject', 'description',  'comments', 'ticket_type'
    readonly_fields = ('creation_date',)
   

admin.site.register(TicketLog)
admin.site.register(Category)
admin.site.register(TesteDb)
admin.site.register(Ticket)
admin.site.register(Sla)

