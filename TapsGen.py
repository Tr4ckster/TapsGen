from random import randint as rint

def welcome():
    print("Welcome to TapsGen\n\nPlease type in the amount of symbols you want your password to have.")
    symbol_amount = int(input("Amount (Digits only): "))
    return symbol_amount

def randint():
    if rint(0,1) == 1:
        return True

def passsymbol(name):
    low_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cap_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    symbols = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]",":",";","<",">",",",".","?","/"]
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    if name == "low_letters":
        return low_letters[rint(0,len(low_letters)-1)]
    if name == "cap_letters":
        return cap_letters[rint(0,len(cap_letters)-1)]
    if name == "symbols":
        return symbols[rint(0,len(symbols)-1)]
    if name == "nums":
        return nums[rint(0,len(nums)-1)]

def pwkind():
    print("--------")
    print("What symbols do you want your Password to contain?")
    print("0 - Letters only")
    print("1 - Special Symbols only")
    print("2 - Numbers only")
    print("3 - Letters and Special Symbols")
    print("4 - Letters and Numbers")
    print("5 - Numbers and Special Symbols")
    print("6 - Letters, Special Symbols and Numbers")
    print("--------")
    kind = int(input("Type the correspondending Number for the Symbols to be added in the Password: \n"))
    return kind
    

def pwgen(symamount=8, pwkind=6):
    pw = []
    if pwkind > 6:
        print("The Number you provided is not a Number from the Selection Menu!")
    else:
        for symbol in range(symamount):
            if pwkind == 0:
                if randint():
                    pwsymbol = passsymbol("low_letters")
                else:
                    pwsymbol = passsymbol("cap_letters")
            if pwkind == 1:
                pwsymbol = passsymbol("symbols")
            if pwkind == 2:
                pwsymbol = passsymbol("nums")
            if pwkind == 3:
                if randint():
                    pwsymbol = passsymbol("symbols")
                else:
                    if randint():
                        pwsymbol = passsymbol("low_letters")
                    else:
                        pwsymbol = passsymbol("cap_letters")
            if pwkind == 4:
                if randint():
                    pwsymbol = passsymbol("nums")
                else:
                    if randint():
                        pwsymbol = passsymbol("low_letters")
                    else:
                        pwsymbol = passsymbol("cap_letters")
            if pwkind == 5:
                if randint():
                    pwsymbol = passsymbol("nums")
                else:
                    pwsymbol = passsymbol("symbols")
            if pwkind == 6:
                random = rint(0,2)
                if random == 0:
                    if randint():
                        pwsymbol = passsymbol("low_letters")
                    else:
                        pwsymbol = passsymbol("cap_letters")
                elif random == 1:
                    pwsymbol = passsymbol("nums")
                else:
                    pwsymbol = passsymbol("symbols")
            pw.append(pwsymbol)
    print("---------")
    print("Password has been put into Text File")
    return ''.join(pw)

if __name__ == "__main__":
    with open("password.txt", "w") as f:
        f.write(pwgen(welcome(), pwkind()))