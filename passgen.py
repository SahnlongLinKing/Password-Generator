import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
i = 1
while i < 2:
    #Password Generator Project


    print("Let's begin the generation.")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    # final_password = []
    # for number in range(nr_letters):
    #   r_letters = random.randint(0, 25)
    #   final_password.append(letters[r_letters])
    # for number in range(nr_symbols):
    #   r_symbols = random.randint(0, 8)
    #   final_password.append(symbols[r_symbols])
    # for number in range(nr_numbers):
    #   r_numbers = random.randint(0, 9)
    #   final_password.append(numbers[r_numbers])
    # print("".join(final_password))

    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    draft_password = []
    for number in range(nr_letters):
        r_letters = random.randint(0, 25)
        draft_password.append(letters[r_letters])
    for number in range(nr_symbols):
        r_symbols = random.randint(0, 8)
        draft_password.append(symbols[r_symbols])
    for number in range(nr_numbers):
        r_numbers = random.randint(0, 9)
        draft_password.append(numbers[r_numbers])
    random.shuffle(draft_password)
    final_password = "".join(draft_password)
    print(f"Your password is: {final_password}")
    generatenew = input("Generate another? Y/N\n")
    if generatenew == "Y":
        generatenew == True
    else:
        generatenew == False
    if generatenew == False:
        i += 1
    else:
        i = 1