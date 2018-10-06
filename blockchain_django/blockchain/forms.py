from django import forms

class TransactionForm(forms.Form):
    tx_data = forms.CharField(label='Transaction data', max_length=100)