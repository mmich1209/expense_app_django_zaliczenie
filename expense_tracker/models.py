from django.db import models

# Create your models here.
#model for saving up the expenses

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name