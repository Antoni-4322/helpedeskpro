# Generated by Django 5.0.6 on 2024-06-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_workdesk_name_workdesk_parent_workdesk_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='workdesk',
            name='name',
            field=models.CharField(max_length=65, null=True),
        ),
    ]
