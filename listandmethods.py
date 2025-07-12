# list are mutable meaning they can be modified

list1 = ['xyz',332,53,'x',False]
list1[-1]=True
list1[1]='Yes'
print('List value : ',list1)

#slicing a list
print('slice from list1 : ',list1[2:-1])