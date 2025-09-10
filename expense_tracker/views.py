from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from django.db.models.functions import TruncDate
import datetime


# Create your views here.

def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))

    # calculating 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    one_year_data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = one_year_data.aggregate(Sum('amount'))

    # calculating 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    one_month_data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = one_month_data.aggregate(Sum('amount'))

    # calculating last week expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    one_week_data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = one_week_data.aggregate(Sum('amount'))

    #calculating categorical expenses
    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))

    # calculating daily expenses
    daily_sums = Expense.objects.annotate(day=TruncDate('date')).values('day').annotate(sum=Sum('amount')).order_by('day')


    expense_form = ExpenseForm()
    return render(request, 'expense_tracker/index.html',
                  {'expense_form': expense_form,
                   'expenses': expenses,
                   'total_expenses': total_expenses,
                   'yearly_sum': yearly_sum,
                   'monthly_sum': monthly_sum,
                   'weekly_sum' : weekly_sum,
                   'daily_sums': daily_sums,
                   'categorical_sums': categorical_sums})


def delete(request, id):
    if request.method == 'POST' and 'delete' in request.POST:  # checking if the POST request comes from delete button
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')


def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense.save()
            return redirect('index')
    return render(request, 'expense_tracker/edit.html', {'expense_form': expense_form})
