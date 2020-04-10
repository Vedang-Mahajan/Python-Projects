correct=0

Balance=1000

loan=0

print("Welcome to TechClub International Bank.")
a=int(input("Please Enter your Account Number: "))

if a==246801:
    correct=correct+1
    
while correct==1:
    b=input("Enter your Password: ")
    
    if b=="password":
        print(" ")
        print("Welcome Vedang!")
        print(" ")
        correct=correct+1
        break
while correct==2:
    print(" ")
    print("What would you like to do?")
    print(" ")
    print("1) Balance Inquiry")
    print("2) Cash Deposit")
    print("3) Cash Withdrawal")
    print("4) Loan")
    print("5) Quit")
    print(" ")
    c=int(input("Enter the option number of the task you would like to do: "))
    
    if c==1:
        correct=correct+1
        print(" ")
        print("Your current balance is ₹" +str(Balance) +".")
        print(" ")
        print("Press 'B' to go back")
        print(" ")
        d=input("Your answer: ")
        
        if d=="B" or d=="b":
            correct=correct-1
            
    if c==2:
        correct=correct+1
        print(" ")
        e=int(input("Enter the amount you want to deposit (Maximum ₹5000): ₹"))
        Balance=Balance+e
        print(" ")
        print("Amount Deposited successfully!")
        print("Check your balance for current amount.")
        print(" ")
        print("Press 'B' to go back")
        print(" ")
        f=input("Your answer: ")
        
        if f=="B" or f=="b":
            correct=correct-1
            
    if c==3:
        correct=correct+1
        print(" ")
        g=int(input("Enter the amount you want to withdraw (Maximum ₹" +str(Balance-10) +"): ₹"))
        Balance=Balance-g
        print(" ")
        print("Amount Withdrawn successfully!")
        print("Check your balance for current amount.")
        print(" ")
        print("Press 'B' to go back")
        print(" ")
        h=input("Your answer: ")
        
        if h=="B" or h=="b":
            correct=correct-1
            
    if c==4:
        correct=correct+1
        loan=loan+1
        while loan==1:
            print("Welcome! Here you can opt for a loan if you would like to.")
            print(" ")
            print("Press 'B' to go back")
            print("Press 'C' to Continue")
            print(" ")
            z=input("Your answer: ")
        
            if z=="B" or z=="b":
                loan=loan-1
                correct=correct-1
            elif z=="C" or z=="c":
                    loan = loan+1
            while loan==2:
                i=int(input("Enter your loan amount (Maximum ₹" +str(Balance/2) +"): ₹"))
                print(" ")
                j=input("Are you sure you want to proceed? ")
                
                if j=="yes" or j=="Yes":
                    print(" ")
                    print("Congratulations!")
                    print("Loan has been opted by you.")
                    Balance=Balance-i
                    loan=loan-2
                    correct=correct-1
                elif j=="no" or j=="No":
                    print("Process Cancelled!")
                    loan=loan-2
                    
    
    if c==5:
        correct=correct+1
        s=input("Are you sure you want to quit? ")
        
        if s=="no" or s=="No":
            correct=correct-1
        elif s=="yes" or "Yes":
            break
            
print(" ")
print("Thank you For visiting TechClub International Bank!")
print(" ")
print("Have a great day!")
