from django.db import models

# Create your models here.
class LotoMachine(models.Model):
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Peripherals(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    loto_machine_id = models.ForeignKey(LotoMachine, on_delete=models.CASCADE)
