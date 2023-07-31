from django.forms import ModelForm
from .models import Account, Transaction


# Creates account form below based on account model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Creates transaction form based on Transaction Model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
