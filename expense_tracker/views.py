from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm


# Create your views here.

def index(request):
    expense_form = ExpenseForm()
    return render(request, 'expense_tracker/index.html', {'expense_form': expense_form})

