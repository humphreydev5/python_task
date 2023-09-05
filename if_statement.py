x = int(input("Please enter an integer: "))
#Please enter an integer: 42
if x < 0:
    x = 0
    print('The negative changes to zero')
elif x == 0:
    print('This is a Zero value')
elif x == 1:
    print('This is a Single value')
else:
    print('More value')