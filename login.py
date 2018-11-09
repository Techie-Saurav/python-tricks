print("----Welcome!----")
print

username = ""
passcode = 0

def login():        #defined login command
    username = raw_input("Enter username:")
    #username entry

    passcode = input("Enter passcode{ONLY DIGITS}:")
    #passcode entry

    if username == "administrator":        #username check
        if passcode == 25112004:           #passcode check
            print
            print("________________________________________________")
            print("Access granted!")
            print
            print("Go to https://techie-saurav.github.io")
            print
            print("There will be a QBASIC file containing all that you need. Locate it.")
            print
            print("Good luck, friend.")
            print("________________________________________________")

login()
