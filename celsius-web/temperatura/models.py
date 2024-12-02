from django.db import models
from datetime import datetime

class Temperatura(models.Model):
    temperatura = models.FloatField()
    data = models.DateField(default=datetime.now)
    hora = models.TimeField(default=datetime.now)
    
    def __str__(self):
        return str(self.temperatura)
    


