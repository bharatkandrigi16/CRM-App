# Generated by Django 4.2.4 on 2023-08-21 00:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('importance', models.IntegerField(default=5)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='messageIndex',
            field=models.IntegerField(default=1),
        ),
    ]
