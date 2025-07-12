# sets have unique value and they are mutable

set_a = {3,23,76,3,32}
set_b = {9,4,43,6,65,4}

print('value of set_a : ',set_a)
print('value of set_b : ',set_b)

set_a.add(2)
print('value of set_a after adding 2 : ',set_a)

print('value of set_b after pop : ',set_b.pop())

set_c = set_a.union(set_b)
print('value of after intersecting  : ',set_c)

