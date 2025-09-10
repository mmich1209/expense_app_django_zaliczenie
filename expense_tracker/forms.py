from django.forms import ModelForm
from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'category')

    def clean_category(self):
        category = self.cleaned_data['category']
        return category.strip().capitalize()
