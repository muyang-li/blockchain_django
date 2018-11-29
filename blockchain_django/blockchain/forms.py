from django import forms

# class TransactionForm(forms.Form):
#     tx_data = forms.CharField(label='Transaction data', max_length=100)

# class IndexQueryForm(forms.Form):
#     index = forms.IntegerField()

class IdQueryForm(forms.Form):
    uid = forms.CharField(label='Identity Number', max_length=13)

