# Generated by Django 5.0.6 on 2024-06-28 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_remove_ticketlog_type_ticketlog_log_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketlog',
            old_name='id_user',
            new_name='user_id',
        ),
    ]
