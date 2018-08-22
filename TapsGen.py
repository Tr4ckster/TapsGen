from random import randint

def choosesymbols(lenght):
    # CODE THAT ASKS IF USER WANTS TO USE NUMBERS, LETTERS OR SYMBOLS
    print("Do you want to use Numbers, Letters or Symbols? Or all together?")
    print("----------------------")
    print("1 - Only Letters")
    print("2 - Only Numbers")
    print("3 - Only Symbols")
    print("4 - Letters and Numbers")
    print("5 - Letters and Symbols")
    print("6 - Numbers and Symbols")
    print("7 - All of them together")
    print("----------------------")
    choose = int(input("Choose from one of the Numbers "))
    if choose > 7:
        choose = int(input("The Number you typed in is too big. Please use 1-7 "))
        choosesymbols(lenght)
    else:
        generate_password(lenght,choose)

def welcome_to_tapsgen():
    print("----------------------")
    print("Welcome to TapsGen. A easy to use Password Generator.")
    print("How long do you want your password to be? It should be atleast 8 Symbols.")
    print("But the more the better.")
    print("----------------------")
    lenght = int(input("Please type in the amount of symbols you want to have. (Only use Digits 0-9) "))
    if lenght < 8:
        confirmshortpw = input("Are you sure you want your Password only have {} Symbols? This might be easy to crack. Y/N ".format(lenght)).lower()
        if confirmshortpw == "y":
            choosesymbols(lenght)
        else:
            welcome_to_tapsgen()
    else:
        print("You want your Password to have {} Symbols. ".format(lenght))
        confirm = input("Is that correct? Y/N ").lower()
        if confirm == "y":
            choosesymbols(lenght)
        else:
            welcome_to_tapsgen()

def generate_password(lenght,choose):
    letters_cap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    nums = range(0,9)
    symbols = ["#","@","/","§","%","!","=","*","+","~","-","<",">"]
    password = []
    for symbol in range(0,lenght):
        randomizer_letters_cap = randint(0,len(letters_cap)-1)
        password.append(letters_cap[randomizer_letters_cap])
    print("Your password is: \n")
    print("".join(password))

welcome_to_tapsgen()
