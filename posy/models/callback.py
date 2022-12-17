from django.db import models


class Callback(models.Model):
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.phone_number} - {self.created}'
