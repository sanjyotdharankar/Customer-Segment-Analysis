from django import forms

class ModelUploadForm(forms.Form):
    recency = forms.IntegerField(label='Recency')
    total_expenses = forms.FloatField(label='Total Expenses')
    income = forms.FloatField(label='Income')
    total_acc_cmp = forms.FloatField(label='Total Acc Cmp')
    total_purchases = forms.FloatField(label='Total Purchases')
    