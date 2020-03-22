# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:24:59 2020

@author: Administrator
"""

correct=0
correct1=0
correct2=0
correct3=0

Balance=1000
Balance1=1000
Balance2=1000
Balance3=1000

loan=0
loan1=0
loan2=0
loan3=0

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
        
elif a==135790:
    correct1=correct1+1
    
    while correct1==1:
        b=input("Enter your Password: ")
    
        if b=="password":
            print(" ")
            print("Welcome Shreyas!")
            print(" ")
            correct1=correct1+1
            break
    while correct1==2:
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
            correct1=correct1+1
            print(" ")
            print("Your current balance is ₹" +str(Balance1) +".")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            d=input("Your answer: ")
        
            if d=="B" or d=="b":
                correct1=correct1-1
            
        if c==2:
            correct1=correct1+1
            print(" ")
            e=int(input("Enter the amount you want to deposit (Maximum ₹5000): ₹"))
            Balance1=Balance1+e
            print(" ")
            print("Amount Deposited successfully!")
            print("Check your balance for current amount.")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            f=input("Your answer: ")
        
            if f=="B" or f=="b":
                correct1=correct1-1
            
        if c==3:
            correct1=correct1+1
            print(" ")
            g=int(input("Enter the amount you want to withdraw (Maximum ₹" +str(Balance1-10) +"): ₹"))
            Balance1=Balance1-g
            print(" ")
            print("Amount Withdrawn successfully!")
            print("Check your balance for current amount.")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            h=input("Your answer: ")
        
            if h=="B" or h=="b":
                correct1=correct1-1
            
        if c==4:
            correct1=correct1+1
            loan1=loan1+1
            while loan1==1:
                print("Welcome! Here you can opt for a loan if you would like to.")
                print(" ")
                print("Press 'B' to go back")
                print("Press 'C' to Continue")
                print(" ")
                z=input("Your answer: ")
            
                if z=="B" or z=="b":
                    loan1=loan1-1
                    correct1=correct1-1
                elif z=="C" or z=="c":
                    loan1 = loan1+1
                while loan1==2:
                    i=int(input("Enter your loan amount (Maximum ₹" +str(Balance1/2) +"): ₹"))
                    print(" ")
                    j=input("Are you sure you want to proceed? ")
                
                    if j=="yes" or j=="Yes":
                        print(" ")
                        print("Congratulations!")
                        print("Loan has been opted by you.")
                        Balance1=Balance1-i
                        loan1=loan1-2
                        correct1=correct1-1
                    elif j=="no" or j=="No":
                        print("Process Cancelled!")
                        loan1=loan1-2
                    
    
        if c==5:
            correct1=correct1+1
            s=input("Are you sure you want to quit? ")
        
            if s=="no" or s=="No":
                correct1=correct1-1
            elif s=="yes" or "Yes":
                break
            
        print(" ")
        print("Thank you For visiting TechClub International Bank!")
        print(" ")
        print("Have a great day!")
        
        
elif a==123456:
    correct2=correct2+1
    
    while correct2==1:
        b=input("Enter your Password: ")
    
        if b=="password":
            print(" ")
            print("Welcome Aryaman!")
            print(" ")
            correct2=correct2+1
            break
    while correct2==2:
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
            correct2=correct2+1
            print(" ")
            print("Your current balance is ₹" +str(Balance2) +".")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            d=input("Your answer: ")
        
            if d=="B" or d=="b":
                correct2=correct2-1
            
        if c==2:
            correct2=correct2+1
            print(" ")
            e=int(input("Enter the amount you want to deposit (Maximum ₹5000): ₹"))
            Balance2=Balance2+e
            print(" ")
            print("Amount Deposited successfully!")
            print("Check your balance for current amount.")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            f=input("Your answer: ")
        
            if f=="B" or f=="b":
                correct2=correct2-1
            
        if c==3:
            correct2=correct2+1
            print(" ")
            g=int(input("Enter the amount you want to withdraw (Maximum ₹" +str(Balance2-10) +"): ₹"))
            Balance2=Balance2-g
            print(" ")
            print("Amount Withdrawn successfully!")
            print("Check your balance for current amount.")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            h=input("Your answer: ")
        
            if h=="B" or h=="b":
                correct2=correct2-1
            
        if c==4:
            correct2=correct2+1
            loan2=loan2+1
            while loan2==1:
                print("Welcome! Here you can opt for a loan if you would like to.")
                print(" ")
                print("Press 'B' to go back")
                print("Press 'C' to Continue")
                print(" ")
                z=input("Your answer: ")
            
                if z=="B" or z=="b":
                    loan2=loan2-1
                    correct2=correct2-1
                elif z=="C" or z=="c":
                    loan2 = loan2+1
                while loan2==2:
                    i=int(input("Enter your loan amount (Maximum ₹" +str(Balance2/2) +"): ₹"))
                    print(" ")
                    j=input("Are you sure you want to proceed? ")
                
                    if j=="yes" or j=="Yes":
                        print(" ")
                        print("Congratulations!")
                        print("Loan has been opted by you.")
                        Balance2=Balance2-i
                        loan2=loan2-2
                        correct2=correct2-1
                    elif j=="no" or j=="No":
                        print("Process Cancelled!")
                        loan2=loan2-2
                    
    
        if c==5:
            correct2=correct2+1
            s=input("Are you sure you want to quit? ")
        
            if s=="no" or s=="No":
                correct2=correct2-1
        elif s=="yes" or "Yes":
            break
            
        print(" ")
        print("Thank you For visiting TechClub International Bank!")
        print(" ")
        print("Have a great day!")
        
elif a==654321:
    correct3=correct3+1
    
    while correct3==1:
        b=input("Enter your Password: ")
    
        if b=="password":
            print(" ")
            print("Welcome Kabir!")
            print(" ")
            correct3=correct3+1
            break
    while correct3==2:
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
            correct3=correct3+1
            print(" ")
            print("Your current balance is ₹" +str(Balance3) +".")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            d=input("Your answer: ")
        
            if d=="B" or d=="b":
                correct3=correct3-1
            
        if c==2:
            correct3=correct3+1
            print(" ")
            e=int(input("Enter the amount you want to deposit (Maximum ₹5000): ₹"))
            Balance3=Balance3+e
            print(" ")
            print("Amount Deposited successfully!")
            print("Check your balance for current amount.")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            f=input("Your answer: ")
        
            if f=="B" or f=="b":
                correct3=correct3-1
            
        if c==3:
            correct3=correct3+1
            print(" ")
            g=int(input("Enter the amount you want to withdraw (Maximum ₹" +str(Balance3-10) +"): ₹"))
            Balance3=Balance3-g
            print(" ")
            print("Amount Withdrawn successfully!")
            print("Check your balance for current amount.")
            print(" ")
            print("Press 'B' to go back")
            print(" ")
            h=input("Your answer: ")
        
            if h=="B" or h=="b":
                correct3=correct3-1
            
        if c==4:
            correct3=correct3+1
            loan3=loan3+1
            while loan3==1:
                print("Welcome! Here you can opt for a loan if you would like to.")
                print(" ")
                print("Press 'B' to go back")
                print("Press 'C' to Continue")
                print(" ")
                z=input("Your answer: ")
            
                if z=="B" or z=="b":
                    loan3=loan3-1
                    correct3=correct3-1
                elif z=="C" or z=="c":
                    loan3 = loan3+1
                while loan3==2:
                    i=int(input("Enter your loan amount (Maximum ₹" +str(Balance3/2) +"): ₹"))
                    print(" ")
                    j=input("Are you sure you want to proceed? ")
                
                    if j=="yes" or j=="Yes":
                        print(" ")
                        print("Congratulations!")
                        print("Loan has been opted by you.")
                        Balance3=Balance3-i
                        loan3=loan3-2
                        correct3=correct3-1
                    elif j=="no" or j=="No":
                        print("Process Cancelled!")
                        loan3=loan3-2
                    
    
        if c==5:
            correct3=correct3+1
            s=input("Are you sure you want to quit? ")
        
            if s=="no" or s=="No":
                correct3=correct3-1
        elif s=="yes" or "Yes":
            break
            
        print(" ")
        print("Thank you For visiting TechClub International Bank!")
        print(" ")
        print("Have a great day!")
        
else:
    print("Invalid Account Number!")
        
