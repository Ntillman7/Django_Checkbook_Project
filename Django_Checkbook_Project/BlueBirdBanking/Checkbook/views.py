from django.shortcuts import render, redirect
from .forms import AccountForm, TransactionForm


def home(request):
    # this function will render the Home page when requested
    return render(request, 'checkbook/index.html')


def balance(request):
    # this function will render the balance page when requested
    return render(request, 'checkbook/BalanceSheet.html')


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
            form.save()  # save new account
            return redirect('index')  # returns to the home page
        content = {'form': form}  # saves content to the template as dictionary
        # adds content of form to page
        return render(request, 'checkbook/AddTransaction.html', content)

