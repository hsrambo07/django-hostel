from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Warden)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Block)
admin.site.register(Mess)
admin.site.register(LeaveApplication)