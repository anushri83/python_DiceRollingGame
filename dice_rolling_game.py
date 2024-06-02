import random


while True:
    random_number=random.randint(1,6)
    choice=input("Do you want to roll a dice (y/n)")
    if choice.lower()=="n":
        break
    else:
        match(random_number):
            case 1:
                print("------")
                print("     ")
                print("  0  ")
                print("     ")
                print("-----")
            case 2:
                print("------")
                print("0    ")
                print("     ")
                print("    0")
                print("-----")
            case 3:
                print("------")
                print("     ")
                print("0 0 0")
                print("     ")
                print("-----")
            case 4:
                print("------")
                print("0   0")
                print("     ")
                print("0   0")
                print("-----")
            case 5:
                print("------")
                print("0   0")
                print("  0  ")
                print("0   0")
                print("-----")
            case 6:
                print("------")
                print("0 0 0")
                print("     ")
                print("0 0 0")
                print("-----")
            case _:
                print("Enter valid choice")
        