from django.urls import path
from .views import DepositeView,WithdrawView,ListView,LoanListView,LoanRequestView,PayLoanView,TransactionReportView

urlpatterns = [
    path('deposite/',DepositeView.as_view(), name='deposite'),
    path('report/',TransactionReportView.as_view(), name='transaction_report'),
    path('withdraw/',WithdrawView.as_view(), name='withdraw_money'),
    path('loan_request/',LoanRequestView.as_view(), name='loan_request'),
    path('loans/',LoanListView.as_view(), name='loan_list'),
    path('loan/<int:loan_id>/',PayLoanView.as_view(), name='deposite_money'),
]
