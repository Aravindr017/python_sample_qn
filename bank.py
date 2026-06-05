#Case Study - Machine Learning 

# Bank Account Manager

# a. Simulate a bank account with deposit, withdrawal, and balance
# enquiry operations

# b. Use variables and data types to store account information

# c. Implement conditional statements to check for sufficient balance
# before withdrawal

# d. Use functions to perform deposit, withdrawal, and balance inquiry
# operations.



# global Var
current_bal=0

# deposit function
def deposit(Amount):
  global current_bal
  current_bal+=Amount
  print(f'Your updated balance is : {current_bal}')

# withdrawal function
def withdraw(W_Amount):
  global current_bal
  if W_Amount <= current_bal:
    print('Withdrawal in progress...')
    current_bal-=W_Amount
    print(f'Your updated balance is : {current_bal:.2f}')
  else:
    print('Insufficient Balance')
  

#balance checking function 
def balance():
  global current_bal
  print('Checking Balance...')
  print(f'Your Account Balance : {current_bal}')



# main function 
def main():
  print('--Welcome to Bank Account Manager--')
  print(' 1: Deposit Cash \n 2: Withdraw Cash \n 3: Balance Enquiry\n 4: Exit \n')
  while True:
    choice = int(input('Enter the action you want to perform : '))
    if choice == 1:
      Amount = float(input('Enter the amount you want to deposit:'))
      deposit(Amount)
    elif choice == 2:
      W_Amount = float(input('Enter the amount you want to withdraw:'))
      withdraw(W_Amount)
    elif choice == 3:
      balance()
    elif choice == 4:
      print('\n Exited... \n Thank you for using Bank Account Manager \n')
      break
    else:
      print('\nInvalid choice enter the correct choice for perform action \n')
  else:
    print('Code Error')   # for debugging


main()