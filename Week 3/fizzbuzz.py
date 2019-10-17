for n in range (0, 101):
    print(n)
    n = n + 1
    if n%3 == 0 and n%5 == 0:
        print('fizzbuzz')
    elif n%3 == 0 and n%5 != 0:
        print('buzz')
    elif n%3 != 0 and n%5 == 0:
        print('fizz')

#icheated

