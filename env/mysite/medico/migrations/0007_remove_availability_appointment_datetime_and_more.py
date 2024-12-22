# Generated by Django 5.1.1 on 2024-09-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0006_remove_appointment_appointment_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='appointment_datetime',
        ),
        migrations.AddField(
            model_name='availability',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=9),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_datetime',
            field=models.DateTimeField(),
        ),
    ]