from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositeForm,WithdrawForm,LoanRequestForm
from .constants import DEPOSITE,WITHDRAW,LOAN,LOAN_PAID
from django.contrib import messages
# Create your views here.


class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name=''
    model = Transaction
    title=''
    success_url=''
    
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account,
        })
        return kwargs
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })


class DepositeView(TransactionCreateMixin):
    form_class=DepositeForm
    title='Deposite'
    
    def get_initial(self):
        initial={'transaction_type': DEPOSITE}
        return initial
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance += amount
        account.save(
            update_fields=['balance']
        )
        
        messages.success(self.request),f"{amount}$ was deposited to your account successfully"
        return super().form_valid(form)
class WithdrawView(TransactionCreateMixin):
    form_class=WithdrawForm
    title='Withdraw Money'
    
    def get_initial(self):
        initial={'transaction_type': WITHDRAW}
        return initial
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance -= amount
        account.save(
            update_fields=['balance']
        )
        
        messages.success(self.request),f"successfully withdraw {amount}$ from your account"
        return super().form_valid(form)
class WithdrawView(TransactionCreateMixin):
    form_class=LoanRequestForm
    title='Request For Loan'
    
    def get_initial(self):
        initial={'transaction_type': LOAN}
        return initial
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        current_loan_count=Transaction.objects.filter(account=self.request.user.account, transaction_type=3)
        
        
        
        messages.success(self.request),f"successfully withdraw {amount}$ from your account"
        return super().form_valid(form)
class WithdrawView(TransactionCreateMixin):
    form_class=WithdrawForm
    title='Withdraw Money'
    
    def get_initial(self):
        initial={'transaction_type': WITHDRAW}
        return initial
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance -= amount
        account.save(
            update_fields=['balance']
        )
        
        messages.success(self.request),f"successfully withdraw {amount}$ from your account"
        return super().form_valid(form)

