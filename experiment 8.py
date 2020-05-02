class Atm:
    def _init_(self, money):
        self.money=money
        self.name=" Anand Kumar "
        self.number=" 1234 5678 9123 4567"
        self.pin=3401
    def wdraw(self):
        w=int(input("Enter amount: "))
        if(w>10000):
            print(" The amount is exceeding the limit ")
        elif(w>self.money):
            print(" You do not have that much money ")
        else:
            self.money=self.money - w
            print("Account balance: ", self.money)
            print("Please collect your money. Thank you")
    def dept(self):
        d=int(input(" Enter amount: "))
        self.money=self.money + d
        print( "Account balance: ",self.money)
        print(" Thank you ")
    def info(self):
        print("Account Balance: ",self.money )
        print("Name: ",self.name)
        print("Card Number: ",self.number)
    def sys(self):
        i=1
        pn=int(input(" Enter your pin: "))
        while(i):
            if pn == self.pin:
                print(" Enter 1 for Withdrawal. Enter 2 for Deposit. Enter 3 for account info ")
                opt = int(input())
                if opt == 1:
                    a.wdraw()
                    break
                elif opt == 2:
                    a.dept()
                    break
                elif opt == 3:
                    a.info()
                    break
            else:
                if(i!=3):
                    i=i+1
                    pin = int(input(" Wrong pin. Please enter again: "))
                else:
                    print(" You have entered wrong pin code thrice. The account is frozen  ")
                    return -1

a=Atm(10000)
a.sys()
