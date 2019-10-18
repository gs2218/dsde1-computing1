print('How many times a year do you go on holiday')
numHols = input()
try:
    if int(numHols) >= 3:
        print('that is bad for the world')
    elif int(numHols) == 2:
        print('reasonable')
    elif int(numHols) <= 1:
        print('That sounds boring')
except(ValueError):
    print('A number, Fool!')

