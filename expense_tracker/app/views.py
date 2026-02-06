from django.shortcuts import render,redirect 
from .models import Expense
from django.db.models import Sum


# Create your views here.


def add_expense(request):
    if request.method == "POST":
        title = request.POST.get("title")
        amount = request.POST.get("amount")

        Expense.objects.create(
            title=title,
            amount=amount
        )

        return redirect('summary')

    return render(request, "expense.html")


def expense_summary(request):
    expenses = Expense.objects.all()
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, "summary.html", {
        'expenses': expenses,
        'total': total
    })