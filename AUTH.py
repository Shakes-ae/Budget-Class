import random
import time




database = {}

def init():
    print("Welcome to Shakes Bank")

   
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if (haveAccount == 1):            
        login()

    elif(haveAccount == 2):
            
        register()
    else:
        print("You have entered an invalid option")
        init()





def login():
    print("*****Login*****")
    
    acctNo = input("Enter Account Number \n")
    for accountNumber, userDetails in database.items():
        if (accountNumber == acctNo):
            password = input ("Enter password \n")

            if (userDetails[2] == password):
                bankOperation(userDetails)
            else:
                print("invalid password entered")
                login()
        else:
            bankOperation(userDetails)
            
     
        
    


def register():

    print("******Register******")

    
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = (input("Create your password\n"))
    

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, password]
    database.update({"balance": 0.0})


    print("Your Account has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    
    login()



def bankOperation(userDetails):
    print("Welcome  %s %s" %(userDetails[0], userDetails[1]))
    print(time.asctime())

    selectedOption = int(input(("Please select an option: \n  (1) Deposit \n (2) Withdrawal \n (3) Check Balance \n (4) Complain \n (5) Logout \n")))

    if(selectedOption == 1):
        depositOperation()
        bankOperation(userDetails)
    elif(selectedOption == 2):            
        withdrawalOperation()
        bankOperation(userDetails)
    elif(selectedOption == 3):           
         checkBalance()
         bankOperation(userDetails)
    elif(selectedOption == 4):            
        complainOperation()
        bankOperation(userDetails)
    elif(selectedOption == 5):        
        logout()
    else:       
        print("Invalid option selected")
        bankOperation(userDetails)

def checkBalance():
    database.get("balance")
    print("Your balance is %f" % database["balance"])

def depositOperation():
    database.get("balance")
    bal = database.get("balance")
    amt = float(input("Enter amount: \n"))
    bal = amt + bal
    database["balance"] = bal
    print("Transaction completed")
    

def withdrawalOperation():
    amt = float(input("Enter amount \n"))

    bal = database.get("balance")

    if (amt > bal):
        print("insufficient funds. Kindly deposit.")
    else:
        bal = bal - amt
        database["balance"] = bal
        print("Take your cash. Transaction Completed")
   


def complainOperation():
    complain = input("What issue would you like to report? \n")
    print("Thanks for contacting us")

def generateAccountNumber():    
    return random.randrange(1111111111,9999999999)

def logout():
    exit()

init()
