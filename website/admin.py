from django.contrib import admin
from .models import Record, Room, Message

# Register your models here.
admin.site.register(Record)
admin.site.register(Room)
admin.site.register(Message)
