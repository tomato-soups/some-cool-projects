import operator

def final(a, b, c, d, Class):
    m1 = a + b + c + d
    finalg = operator.truediv(int(m1), 4)
    print(f'Your final grade without calcuating mid-term or finals for {Class} is: {finalg}!')