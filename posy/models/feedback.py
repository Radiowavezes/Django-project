from django.db import models


class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    sender = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField(max_length=2000)
    daytime = models.DateTimeField("Time published: ", auto_now_add=True, editable=True)

    def __str__(self):
        return f'{self.full_name} {self.daytime}'
