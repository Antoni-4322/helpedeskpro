# Generated by Django 5.0.6 on 2024-06-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_remove_ticket_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expired', models.BooleanField(default=False)),
                ('ticket_id', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('A', 'Em Espera'), ('B', 'Atendendo'), ('C', 'Pausado'), ('D', 'Concluido')], default='A', max_length=2)),
                ('progress', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
