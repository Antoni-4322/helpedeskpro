# Generated by Django 5.0.6 on 2024-06-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0016_remove_sla_ticket_id_ticket_sla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='sla',
        ),
        migrations.AddField(
            model_name='sla',
            name='ticket_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
