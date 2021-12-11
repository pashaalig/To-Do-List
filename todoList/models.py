from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    status_choices = [
    ('C', 'Completed'),
    ('P', 'Pending'),   
]

    priority_choices =[
        ('1','❶'),
        ('2','❷'),
        ('3','❸'),
        ('4','❹'),
        ('5','❺'),
        ('6','❻'),
        ('7','❼'),
        ('8','❽'),
        ('9','❾'),
        ('10','❿'),
    ]
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    priority = models.CharField(max_length=10, choices=priority_choices)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title 