# Generated by Django 5.1.1 on 2024-09-14 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_appointment_message_alter_appointment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='message',
        ),
    ]
