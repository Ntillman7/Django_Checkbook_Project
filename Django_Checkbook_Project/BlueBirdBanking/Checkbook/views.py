from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


def home(request):
    # this function will render the Home page when requested
    form=TransactionForm(data=request.POST or None)  # retrieve transaction form
    # checks if reqest method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # If the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) # call balance function to render that account's balance sheet
    content= {'form': form} # pass content to the template in dictionary
    # Adds content of form to page
    return render(request, 'checkbook/index.html', content)


def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # Retrieve the requested account using it primary key
    transactions = Transaction.Transactions.filter(account=pk)  # Retrieve all of that account's transactions
    current_total = account.initial_deposit  # creates account total variable, starting from initial deposit value
    table_contents = {}  # creates a dictionary into which transaction information will be placed
    for t in transactions: # loop through transactions to determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # if deposit add money to the balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal subtract money to the balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
    # pass account, account total balance and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    # this function will render the balance page when requested
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the create account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieve The Account form
    # Checks if the request method is POST
    if request.method == 'POST':
        if form.is_valid():  # checks to see if the submitted form is valid
            form.save()  # save new account
        return redirect('index')  # returns to the home page
    content = {'form': form}  # saves content to the template as dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieve The Transaction form
    # Checks if the request method is POST
    if request.method == 'POST':
        if form.is_valid():  # checks to see if the submitted form is valid
            pk = request.POST['account']  # retrieve which account the transaction was for
            form.save()  # save new account
            return balance(request, pk)
        return redirect('index')  # returns to the home page
    content = {'form': form}  # saves content to the template as dictionary
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
