from django.contrib import admin

from .models import LotoMachine, Peripheral

# Register your models here.
class LotoMachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'terminalId', 'password')

class PeripheralAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(LotoMachine, LotoMachineAdmin) 
admin.site.register(Peripheral, PeripheralAdmin)