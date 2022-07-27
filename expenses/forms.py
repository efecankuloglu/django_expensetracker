from django.forms import ModelForm
from django import forms
from .models import ExpenseRecord


class DateInput(forms.DateInput):
    input_type = "date"


class ExpenseForm(ModelForm):
    class Meta:
        model = ExpenseRecord
        fields = ['date', 'location', 'bill_no', 'description', 'in_out', 'amount', 'comment']

    amount = forms.FloatField(min_value=0.0)
        
    date = forms.DateField(widget=DateInput())