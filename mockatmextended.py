import random

customer_data = { 2593510798: ['Elis', 'Zade', 'elis@zuri.me', 'elismeme', 452 ] }

def init():

  print("Welcome!")

  have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

  if(have_account == 1):
   login()

  elif(have_account == 2):
   print(register())

  else:
   print("You have selected invalid option")
   init()


def login():

  print('You made it!')

  user_acc_number = int(input('Account number \n'))
  password = input('Account password \n')

  for acc_number, userDetails in customer_data.items():
      if(acc_number == user_acc_number):
        if(userDetails[3] == password):
          atm_ops(userDetails)

  print('Login unsuccessful')
  login()
  
def register():

    email = input('Insert valid email \n')
    first_name = input('First name \n')
    last_name = input('Last name \n')
    password = input('Insert password \n')

    acc_number = new_acc_number()

    customer_data[acc_number] = [ first_name, last_name, email, password ]

    print('Your account number is: %d ' % acc_number)

    login()

    
def new_acc_number():
    return random.randrange(1111111111, 9999999999)         

def atm_ops(user):

  print('Atm Operations for: %s %s' % (user[0], user[1]))
  
  selected_option = int(input('Please select an option: 1.) Withdraw 2.) Deposit 3.) Logout \n'))

  if(selected_option == 1):
    atm_withdraw()

  elif(selected_option == 2):
    atm_deposit()

  elif(selected_option == 3):
    login()  

  elif(selected_option == 4):
    exit()

  else:
    print('Invalid Selection')
    atm_ops(user)

def atm_withdraw():
  print('Atm Withdrawal')
  cashwithdrawn = int(input('How much would you like to withdraw \n'))
  print ('Take your cash')

def atm_deposit():
  print('Atm Deposit')
  cashreceived = int(input('How much would you like to deposit? '))
  print (cashreceived)

def acc_balance(userDetails):
    return userDetails[4]
    

init()