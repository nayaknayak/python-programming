print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print(" 4. Exit")

principle = 50000.00
i=1
while i <= 3:
 choice = int(input("Enter your Transaction ? "))


 match choice:
    case 1:
        print(principle)
    case 2:
        deposite = float(input("Enter how much you want to deposite ?"))
        principle=principle+deposite
        print("you have deposite", deposite,
              " your Total balance is ", principle)
    case 3:
        withdraw = float(input("Enter How much you want to Withdraw ? "))
        if principle > 0 and principle > withdraw:
            principle=principle-withdraw
            print(" your withdraw money is ", withdraw,
                  " and your remaining balance is  ", principle)
          
        else:
            print(
                "you have less money that what you want to withdraw :: your total balance is", principle)
    case 4:
        print("Thank you for using the bank menu. Goodbye!")

    case _:
        print(" Enter a valid  keyword from avobe options")
 i=i+1