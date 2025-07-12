# for handling unexpected errors we used try except

try:
    a = int(input('Enter you rank : '))
    print("rank is : ",a)
except Exception as e:
    print('Some error occured : ', e)


# now checking for string
try:
    a = str(input('Enter you name : '))
    print("Name is : ",a)
except Exception as e:
    print('Some error occured : ', e)
