#For  Stopping Program Execution For Some Time
import time
print("Please insert your ATM CARD")

#For Card Processing
time .sleep(5)

#Taking ATM Pin From User
pin=int(input("enter your 4 digit ATM Pin"))

#User Account Balance
balance = 5000

#Checking Pin Is Valid Or Not
if pin== 1234:

#Loop Will Run User Get Free
     while True:

#Showing Info To User
          print("""
                 1 == balance
                 2 == withdraw balance
                 3 == deposit balance 
                 4 == exit
                 """
               )

          try:

#Taking An Option From User
               option = int(input("Choose any option above"))
          except:
               print("Please Choose the valid  option")

#For Option 1
          if option == 1:
              print(f"Your current balance is {balance}")

          if option == 2:
              withdraw_amount = int(input("please enter withdraw_amount"))
              balance = balance - withdraw_amount

              print(f"{withdraw_amount}is debited  from your account")

              print(f"your updated balance is {balance}")

          if option == 3:


               deposit_amount = int(input("please enter deposit_amount"))

               balance = balance + deposit_amount

               print(f"{deposit_amount}is credited to your account")

               print(f"your updated balance is {balance}")

          if option == 4:

           break

else:
    print("wrong pin Please try again")
