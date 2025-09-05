from django.db import models

# Create your models here.

# Model for saving up the expense
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name