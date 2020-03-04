import secrets

def choosesymbols(length):
    # CODE THAT ASKS IF USER WANTS TO USE NUMBERS, LETTERS OR SYMBOLS
    print("Do you want to use Numbers, Letters or Special symbols? Maybe all of the above?")
    print("----------------------")
    print("1 - Only Letters")
    print("2 - Only Numbers")
    print("3 - Only Special symbols")
    print("4 - Letters and Numbers")
    print("5 - Letters and Special symbols")
    print("6 - Numbers and Special symbols")
    print("7 - All of them")
    print("----------------------")
    choice = int(input("Choose from one of the numbers: "))
    if choice > 7:
        print("That number isn't on the list. Please try again")
        choosesymbols(length)
    else:
        generate_password(length,modeselect(choice))

def modeselect(choice):
    # Code that selects the character set for the password
    letts = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    syms = ["~","!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}",":",";","'",'"',"\\","|",",",".","/","<",">","?"]
    if choice in (1,0): sym_set = letts 
    if choice==2: sym_set = nums
    if choice==3: sym_set = syms 
    if choice==4: sym_set = letts+nums
    if choice==5: sym_set = letts+syms 
    if choice==6: sym_set = nums+syms
    if choice==7: sym_set = letts+nums+syms
    return(sym_set)


def welcome_to_tapsgen():
    print("----------------------")
    print("Welcome to TapsGen. An easy to use Password Generator.")
    print("How long do you want your password to be? It should be at least 8 symbols.")
    print("But the more, the better.")
    print("----------------------")
    length = int(input("Please type in the amount of symbols you want to have. (Only use Digits, 0-9)\n"))
    if length < 8:
        confirmshortpw = input("Are you sure you want your password only have {} symbols? This might be easy to crack. Y/N\n".format(length)).lower()
        if confirmshortpw == "y":
            choosesymbols(length)
        else:
            welcome_to_tapsgen()
    else:
        print("You want your password to have {} symbols. ".format(length))
        confirm = input("Is that correct? Y/N\n").lower()
        if confirm == "y":
            choosesymbols(length)
        else:
            welcome_to_tapsgen()

def generate_password(length,sym_set):
    password = []
    for symbol in range(0,length): password.append(secrets.choice(sym_set))
    print("\nYour password is:")
    print("-" * length)
    print("".join(password))
    print("-" * length)

welcome_to_tapsgen()
