# Easy paisa script
user_choice = input("Enter a number : ")
months = int(input("Enter months: "))
while(user_choice != 'q'):
    user_choice = int(user_choice)
    for i in range(months):
        for i in range(4):
            user_choice -= 220
            print(user_choice, end=" - ")
            user_choice += 28
            print(user_choice, end="\n")
        print()

    user_choice = input("Enter a number : ")
    months = int(input("Enter months: "))
