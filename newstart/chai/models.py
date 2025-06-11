from django.db import models
from django.utils import  timezone 
#utils is a class through which we can add extra feature or help the task to  and make faster and easier


# Create your models here.
class chaivariety(models.Model):
    Chai_Types_Choices=[
        ('MT','Masala'),
        ('LT','lemon'),
        ('GT','ginger'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chai/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2, choices=Chai_Types_Choices)
    description=models.TextField(default='empty')


    def __str__(self):
     return self.name