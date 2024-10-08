# Generated by Django 5.0.6 on 2024-06-23 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_workdesk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workdesk',
            name='name',
        ),
        migrations.AddField(
            model_name='workdesk',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='account.workdesk'),
        ),
        migrations.AddField(
            model_name='workdesk',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
