from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .forms import ExpenseForm
from .models import ExpenseRecord


class MainPageView(View):
    def get(self, request):
        form = ExpenseForm()
        qs = ExpenseRecord.objects.order_by('date')
        total = 0
        for i in qs:
            if i.in_out == "Out":
                total -= i.amount
            elif i.in_out == "In":
                total += i.amount


        context = {'form': form, 'qs': qs, "total": total}

        return render(request, 'main_page.html', context=context)

    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main_page')


def update_expense(request, pk):
    expense = ExpenseRecord.objects.get(id=pk)

    form = ExpenseForm(instance=expense)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('main_page')

    return render(request, 'update_page.html', {'expense_edit_form': form})
    

class ExpenseDeleteView(DeleteView):
    model = ExpenseRecord
    template_name = 'delete_page.html'
    success_url = reverse_lazy('main_page')