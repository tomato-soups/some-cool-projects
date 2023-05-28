import operator

def GPA(amount, scale=4):
    """
    Calculates the GPA of a student.
    
    Parameters
    ----------
    n : int
        The number of credits earned.
    scale : int, optional
        The number of credits in a semester.
    
    Returns
    -------
    gpa : float
        The GPA of the student.
    """
    grades = []
    i = 1
    m = 0
    while int(m) < amount:
        try: 
            
            e = float(input(f"Please enter the grade for class {i}: "))
            if e < 0 or e > 100:
                print("Please enter a number between 0 and 100")
            else:
                grades.append(e)
                i += 1
                m += 1
        except ValueError:
            print("Please enter valid input")
    total = 0
    for b in grades:
        total = operator.add(total, b)
    avg = total / len(grades)
    nonescale = operator.truediv(avg, 100)
    scaled = operator.mul(nonescale, scale)
    print(f'Your GPA on {float(scale)} scale is {round(scaled, 2)}')