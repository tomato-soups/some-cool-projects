import baseAvg
import GPA

types = ('baseAverage', 'GPA')

i = True
while i is True:
    inputType = input(f"Enter the type of calcuation from the list. THE LIST IS CASE SENSITIVE! {types}: ")
    if inputType not in types:
        print(f"{inputType} is not a valid option.")
    else:
        i = False
        break

if inputType == 'baseAverage':

    Class = input(f"Enter the name of the class: ")

    m = False
    n = False
    k = False
    l = False


    while m is False: 
        try:
            q1 = float(input('Enter your grade for quarter 1: '))
            if q1 < 0 or q1 > 100:
                print("Please enter a number above 0 or below 100")
            else:
                m = True
        except ValueError:
            print("Please enter a number")
            continue
    while n is False: 
        try:
            q2 = float(input('Enter your grade for quarter 2: '))
            if q2 < 0 or q2 > 100:
                print("Please enter a number above 0 or below 100")
            else:
                n = True
        except ValueError:
            print("Please enter a number")
            continue
    while k is False: 
        try:
            q3 = float(input('Enter your grade for quarter 3: '))
            if q3 < 0 or q3 > 100:
                print("Please enter a number above 0 or below 100")
            else:
                k = True
        except ValueError:
            print("Please enter a number")
            continue
    while l is False:
        try:
            q4 = float(input('Enter your grade for quarter 4: '))
            if q4 < 0 or q4 > 100:
                print("Please enter a number above 0 or below 100")
            else:
                l = True
        except ValueError:
            print("Please enter a number")
            continue

    baseAvg.final(q1, q2, q3, q4, Class)
elif inputType == 'GPA':
    i = False
    c = False

    while i is False:
        n = input("Enter the amount of classes: ")
        try:
            int(n)
            
            i = True
        except ValueError:
            print("Please enter a number")
    amount = int(n)
    while c is False:
        try:
            p = int(input("Enter the scale you want to calcucate: "))
            if p < 2 or p > 6:
                print("Please enter a scale between 6 and 2")
            else:
                c = True
        except ValueError:
            print("Invalid Input")
    scale = int(p)
        
        
    GPA.GPA(amount, scale)
