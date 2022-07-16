from django.urls import path
from .views import *
from loanApp import views


app_name = 'loanApp'
urlpatterns = [
    path('loan-request/', views.LoanRequest, name='loan_request'),
    path('loan-payment/', views.LoanPayment, name='loan_payment'),
    path('user-transaction/', views.UserTransaction, name='user_transaction'),
    path('user-loan-history/', views.UserLoanHistory, name='user_loan_history'),
    path('user-dashboard/', views.UserDashboard, name='user_dashboard'),
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),

]
