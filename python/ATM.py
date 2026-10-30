def show_menu():
    print('1.check_balance')
    print('2.deposit')
    print('3.withdraw')
    print('4.Exit')

    while True:
        choice=input("Enter your Choice: ")
        if choice=="1":
            check_balance()
        elif choice=="2":
            deposit()
        elif choice=="3":
            withdraw()
        elif choice=="4":
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice.please try again.")
        

balance=10000

def check_balance():
    print("Available balance:",balance)


def deposit():
    global balance
    amount=float(input("Enter deposit amount: "))
    if amount<=0:
        print("please enter a valid amount")
    else:
        balance += amount
        print("Amount deposited sucessfully")
        print("updated balance: ",balance)
        check_balance()
def withdraw():
    global balance
    amount=float(input("Enter withdraw amount: "))
    if amount<=0:
        print("please enter a valid amount")

+63    elif amount>balance:
        print("insufficient funds!")
        
    else:
        balance -= amount
        print("Amount withdraw sucessfully")
        print("remaining balance: ",balance)
        check_balance()


show_menu()
           
 
