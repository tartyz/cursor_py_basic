
#         (1)
#         lst = []
#         for num in range(10):
#             if num % 2 == 1:
#                 lst.append(num ** 2)
#             else:
#                lst.append(num ** 4)
#        print(lst)
#       (2)
#        list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

print ("12. Convert (1) to list comprehension")
print("12 Version 1:")
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
print ("12 List comprihension version:")

lst_1 = [num ** 2  if num %2 == 1 else num ** 4 for num in range (10)]

print (lst_1)
print ("13. Convert (2) to regular for with if-else:")
print("13 list_comprehension:")
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print (list_comprehension)
print ("13 Converted version:")
lst = []
for num in range (10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num*10)
print (lst)
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
#

print ("# 14. Convert (3) to dict comprehension:")
print ("14 initial method (3):")
d = {}
for num in range(1, 11):
     if num % 2 == 1:
         d[num] = num ** 2
print(d)
print ("14 converted to list of comprihension method (3):")
dict_1 = {num ** 2 if num % 2 == 1 in range (1, 11)}
print (dict_1)
# 15*. Convert (4) to dict comprehension.
# 16. Convert (5) to regular for with if.
# 17*. Convert (6) to regular for with if-else.