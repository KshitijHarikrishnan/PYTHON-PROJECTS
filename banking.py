def showBalance(amount):
    print(f"Your current balance is: ${amount}")

def deposit():
    depositAmount = float(input("Enter the deposit amount: $"))
    #float(depositAmount)

    if depositAmount <= 0:
        print("INVALID AMOUNT")
        return 0
    else:
        return depositAmount

def withdraw(amount):
    withdrawAmount = float(input("Enter the withdraw amount: $"))
    
    if withdrawAmount < 0:
        print("INVALID AMOUNT")
        return 0
    elif withdrawAmount > amount:
        print("INSUFFIECIENT FUNDS")    
        return 0
    else:
        return withdrawAmount      


def main():
    balance = 0

    while True:
        print("BANKING PROGRAM")
        print("1. SHOW BALANCE")
        print("2. DEPOSIT AMOUNT")
        print("3. WITHDRAW AMOUNT")
        print("4. EXIT PROGRAM")

        choice = str(input("Enter your choice from  1-4: "))

        if choice == "1":
            showBalance(balance)
        elif choice == "2":
            balance += deposit() 
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            break
        else:
            print("INVALID CHOICE")   

if __name__ == '__main__':
    main()            





