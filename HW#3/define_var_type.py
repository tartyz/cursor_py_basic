# 1. Define the id of next variables:
int_a = 55 # integer
str_b = 'cursor' # string
set_c = {1, 2, 3} # set
lst_d = [1, 2, 3] # list
dict_e = {'a': 1, 'b': 2, 'c': 3} # dictionary
print("1.defiition of variables:")
print("[int_a id is:",id(int_a),
      "] [str_b id is:",id(str_b),
      "] [set_c id is:",id(set_c),
      "] [lst_d id is:",id(lst_d),
      "] [dict_e id is:",id(dict_e),
      "]")
print()


#2. Append 4 and 5 to the lst_d and define the id one more time.
apdt = [4, 5]
lst_d.append(apdt)
print("2. Append 4 and 5 to the lst_d and define the id one more time result is:")
print("a) Appended 4 and 5 to lst_d result :",lst_d)
print()
print("b) Redefinition of id is:")
print("[int_a id is:",id(int_a),
      "] [str_b id is:",id(str_b),
      "] [set_c id is:",id(set_c),
      "] [lst_d id is:",id(lst_d),
      "] [dict_e id is:",id(dict_e),
      "]")
print()

# 3. Define the type of each object from step 1.
print("3. Define the type of each object from step 1 result is: ")
print("[Variable int_a is : ", type(int_a),
      "] [Variable str_b is : ", type(str_b),
      "] [Variable set_c is : ", type(set_c),
      "] [Variable lst_d is : ", type(lst_d),
      "] [Variable dict_e is : ", type(dict_e),
      "]")
print()
#4*. Check the type of the objects by using isinstance.

print("4*.Types of the objects by using isinstance is:")
def classtypeisinstance(classtype):
    if isinstance(classtype,int)==True :
        return(" is int")
    else:
        if isinstance(classtype,str)==True :
            return(" is str")
        else:
            if isinstance(classtype, set) == True:
                return(" is set")
            else:
                if isinstance(classtype, list) == True:
                    return(" is list")
                else:
                    if isinstance(classtype, dict) == True:
                        return(" is dict")
                    else:
                        return(" class is not confirmed")

print ("[int_a :",classtypeisinstance(int_a),
       "] [str_b :",classtypeisinstance(str_b),
       "] [set_c :",classtypeisinstance(set_c),
       "] [lst_d :",classtypeisinstance(lst_d),
       "] [dict_e :",classtypeisinstance(dict_e),
       "]")





