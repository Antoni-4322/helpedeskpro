# Generated by Django 5.0.6 on 2024-06-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_alter_ticket_description_alter_ticket_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
