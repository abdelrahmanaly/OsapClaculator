import sqlite3
import webbrowser
import atexit
import os
#the db logs is designed as the following
class Database:
    def __init__(self):
        self.connection = sqlite3.connect("information.db")
    def display(self):
        try:
            value = "select * from logs"
            answer = self.connection.execute(value)
            self.connection.commit()
            return answer
        except:
            print("there is a mistake in the call display")

    def add(self,table_name,value):
        try:
            value = "insert into logs (principal,interest,payment) values (?,?,?)",(temp[0],temp[1],temp[2])
            self.connection.execute(value)
            self.connection.commit()
        except:
            print("there is a mistake in the call")
    def sum_payments(self):
        try:
            value = "select sum(payment) from logs where payment <> 0 || payment <> null"
            answer = self.connection.execute(value)
            self.connection.commit()
            return answer
        except:
            print("there was an error please try that again.")

    def add_payment_amount(self,amount):
        pass
    def get_current_interest_rate(self):
        pass
    def get_current_principal_rate(self):
        pass
    def goodbye(self):
        self.connection.close()

class Loans(Database):
    #fix this
    def __init__(self,interest_rate,principal):
        super().__init__()
        self.interest_rate = interest_rate
        self.principal = principal

    def getinterest_rate(self):
        return self.interest_rate
    def set_interest_rate(self):
        pass #i need to update the db component
    def get_prinipal(self):
        return self.principal
    def set_principal(self):
        pass #same thing i need to update db component

#variable declarations for use
user_answer=0
answer=[]
while(True):
    try:
        # write to the user if they dont put expected term the system will generate one for them
        print("hello,\n welcome to my program. \n I am going to ask you a few questions in order to be able to help you.\n")
        while(True):
            try:
                user_answer_g = int(input("If you don't know what the jargon means,\n please type 1 if you're comfortable with any financial Questions/Jargon please type 2,\n type any other number if you've already read all of this ?\n"))
                break
            except Exception:
                print("You did not input a proper number, please try again.\n Thank you.\n")
            #not working properly
        if (user_answer_g == 1):
            webbrowser.open('https://www.investopedia.com/terms/l/loan.asp')
            print("Now we got that out of the way, lets see how we can help you out shall we.")
        elif(user_answer_g == 2):
            print('\nAt any moment if you want to exit, just press control c, and i will take care of the rest for you\n')
            print("This progam is supposed to be simple. It's designed for students to have a study way of recording their payments(that isn't on excel) \n")
            print("I don't take any Legal responsability,\n I just want to make a tool that will help out my fellow people.\n Also don't worry i will make it excel Compatible\n")
            print("stay update to date with me or my repo,\n I am more going to keep working on it and message me if you have any ideas\n")
        else:
            while(True):
                try:
                    user_answer = int(input('if you are done reading this page please press 1 to continue: '))
                    if(user_answer == 1):
                        if (os.name == 'Windows'):
                            os.system('cls')
                            break
                        else:
                            os.system('clear')
                            break
                    else:
                        print("Alright I'll wait then")
                except : 
                    print("\nIll just assume this is your way of saying lets go already :D\n")
            print("Please Press 1 if you're setting up or 2 if you're just here to log your Payments.")

            print("Alright, i will ask you a bunch of questions, please answer all of them correctly.\n If you make a mistake type a letter and press continue \n")
            user_answer_principal= int(input("What is the principal amount of the loan ? "))
            user_answer_interst = int(input("What is the interest rate on the loan ? "))
            print("Thank you very much")
            user_answer = int (input('Would you like to record a payment ? if so press 1,\n if you want to see how long it will take you to pay off your loan on your current average monthly payments press2.'))
        #this is how to close the database before the program exits
        #atexit.register(temp.goodbye)
    except KeyboardInterrupt:
        print('\n goodbye :)')
        break
