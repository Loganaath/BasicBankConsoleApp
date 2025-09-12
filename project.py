import random, csv, os, pandas


def GenerateAccountNumber() -> str:
    generate = ""
    for _ in range(0,12):
        generate += str(random.randrange(0,10))
    return generate

def CreateAccount(): #need to be improved
    try:
        print("Create Account:\n")
        name = input("Enter your name: ")
        while True:
            age = int(input("Enter your Age: "))
            if age >= 18 or age <= 100:
                break
            print("Age is Invalid! Try Again.")
        while True:
            ini_deposit = int(input("Enter Amount for your Initial Deposit: "))
            if ini_deposit >= 1000:
                break
            print("Minimum Initial Deposit is 1000 Rupees...")
        account_number = GenerateAccountNumber()

        with open("./acc_number.txt", 'a', encoding='utf-8') as file:
            file.write(f"{name} {account_number}\n")


        Data = [name, account_number, age, ini_deposit]
        file_Exists = os.path.exists("./data.csv")

        #if not file_Exists:
        #    with open("./data.csv", "a", newline="") as file:
        #        write = csv.writer(file)
        #        write.writerow(["Name", "Account_Number", "Age", "Balance"])
        #        write.writerow(Data)

        Dataframe = pandas.read_csv("./data.csv")
        Name = [str(x) for x in Dataframe["Name"].values]
        Account_Number = [str(x) for x in Dataframe["Account_Number"].values]
        Age = [str(x) for x in Dataframe["Age"].values]

        if file_Exists:
            if name in Name or account_number in Account_Number or age in Age:
                print("If is running")
                return 
            else:
                with open("./data.csv", "a", newline="") as file:
                    write = csv.writer(file)
                    write.writerow(Data)        
    except Exception as e:
        return f"Error: {e}"
    
    #return {
    #    name: name,
    #    account_number: account_number,
    #    age: age,
    #    ini_deposit: ini_deposit
    #}

def CheckBalance():
    Data = pandas.read_csv("./data.csv")
    print("Check Balance:\n")
    getInputAcc = int(input("Enter your Account Number: "))
    LengthofAcc = len(str(getInputAcc))
    if LengthofAcc != len(GenerateAccountNumber()):
        print("Invalid Account Number. RETRY!")

    getAccountNumberfromCSV = Data.loc[Data["Account_Number"] == getInputAcc]
    Balance = getAccountNumberfromCSV["Balance"].values
    for i in Balance:
        i = int(i)
        print(f"Your Balance is: {i}")

def Deposit():
    Data = pandas.read_csv("./data.csv")
    print("Deposit:\n")
    getInputAcc = int(input("Enter your Account Number: "))
    LengthofAcc = len(str(getInputAcc))

    if LengthofAcc != len(GenerateAccountNumber()):
        print("Invalid Account Number. RETRY!")


    MinDeposit = 100
    getDepositAmt = int(input("Enter Deposit Amount: "))

    if getDepositAmt < MinDeposit:
        return "Deposit Amount Too Low"

    Data.loc[Data["Account_Number"] == getInputAcc, "Balance"] += getDepositAmt
    Data.to_csv("./data.csv", index=False)
    print(f"{getDepositAmt} Credited to your Account!")

def Withdraw():
    Data = pandas.read_csv("./data.csv")
    print("Withdraw:\n")
    getInputAcc = int(input("Enter your Account Number: "))
    LengthofAcc = len(str(getInputAcc))

    if LengthofAcc != len(GenerateAccountNumber()):
        print("Invalid Account Number. RETRY!")

    MinWithdraw = 100
    getWithdrawAmt = int(input("Enter Withdraw Amount: "))

    if getWithdrawAmt < MinWithdraw:
        return "Withdraw Amount Too Low"

    '''Below is alternative logic'''
    #check = Data.loc[Data["Account_Number"] == getInputAcc, "Balance"].iloc[0]
    check = Data.loc[Data["Account_Number"] == getInputAcc, "Balance"]
    test = int(check.item())

    while True:
        message = "Entered Amount is higher than your Balance"

        if getWithdrawAmt < test:
            Data.loc[Data["Account_Number"] == getInputAcc, "Balance"] -= getWithdrawAmt
            Data.to_csv("./data.csv", index=False)
            break

        print(message)
        return Withdraw()
    print(f"{getWithdrawAmt} Debited from your Account!")

def ShowDetails():
    Data = pandas.read_csv("./data.csv")
    print("Check your Details:\n")
    getAccNo = int(input("Enter your Account Number: "))
    LengthAcc = len(str(getAccNo))

    if LengthAcc != len(GenerateAccountNumber()):
        print("Invalid Account Number. RETRY!")


    Details = Data.loc[Data["Account_Number"] == getAccNo]

    formatting = Details.values

    for i in formatting:
        Name = f"Name: {i[0]}"
        AccNo = f"AccountNumber: {i[1]}"
        Age = f"Age: {i[2]}"
        Balance = f"Balance: {i[3]}"

        print(f"\n{Name}\n{AccNo}\n{Age}\n{Balance}\n")

if __name__ == "__main__":
    file_exists = os.path.exists("./data.csv")
    if not file_exists:
        with open("./data.csv", "a", newline="") as file:
            write = csv.writer(file)
            write.writerow(["Name", "Account_Number", "Age", "Balance"])

    Data = pandas.read_csv("./data.csv")
    check = [Data["Name"].values] # list is easy to access

    def greetNewCustomer():
        print(f"Hello {name}, Welcome to Bank Console.")

    def greetExistingCustomer():
        print(f"Welcome Back {name}! to the Bank Console.")


    name = input("Enter your name: ")


    def features():
        while True:
            features = input(
                "Type any one of these features: 'Deposit', 'Withdraw', 'Balance', 'Details', to access your features! Type 'quit' to exit. >")
            Lower = features.lower()
            lists = ['deposit', 'withdraw', 'balance', 'details', 'quit']

            if Lower in lists:
                if Lower == 'deposit':
                    Deposit()
                elif Lower == 'withdraw':
                    Withdraw()
                elif Lower == 'balance':
                    CheckBalance()
                elif Lower == 'details':
                    ShowDetails()
                elif Lower == 'quit': #need to be improved
                    break

    for i in check:
        if name in i:
            greetExistingCustomer()
            print("Wanna check anything else...")

            features()

            break

        if name not in i:
            greetNewCustomer()

            while True:
                new_customer = input("Type 'create' to create a new account or Type 'quit' to exit: ")
                def WrongInput() -> None:
                    message = "Wrong Input, Type 'create'"
                    print(message)
                    return

                Lower = new_customer.lower()
                lists = ['create', 'quit']

                if new_customer == lists[0]:
                    CreateAccount()
                    features() #need to be improved

                if new_customer == lists[1]:
                    break


