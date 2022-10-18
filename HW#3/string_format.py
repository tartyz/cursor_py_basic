#String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches
#5. With .format and curly braces {}
#6. By passing index numbers into the curly braces.
#7. By using keyword arguments into the curly braces.
#8*. With indicators of field size (5 chars for the first and 3 for the second)
#9. With f-strings and variables
#10. With % operator
#11*. With variable substitutions by name (hint: by using dict)

print("Initial text is: Anna has ___ apples and ___ peaches ")
print()

print("5.Replaced the placeholders with a value with .format and curly braces {} :")
print( "Anna has {} apples and".format(3), "{}peaches.".format(5))
print()
print("6. By passing index numbers into the curly braces:")
print("Anna has {1} apples and {0} peaches".format(5, 3))
print()
print("7. By using keyword arguments into the curly braces:")
print( "Anna has {qty1} apples and {qty2} peaches.".format(qty1=3, qty2=5))
print()
print("#8*. With indicators of field size (5 chars for the first and 3 for the second")
print( "Anna has {0:>5s} apples and {1:>5s} peaches.".format("three", "five"))
print()
print("#9. With f-strings and variables")
apples=3
peaches=5
print( f"Anna has {apples} apples and {peaches} peaches.")
print()
print("#10. With % operator")
apples=3
peaches=5
print( f"Anna has %s apples and %s peaches." % (apples, peaches))
print()
print("11. With variable substitutions by name (hint: by using dict)")
apples=3
peaches=5
fruits_dict = {"a": apples, "p": peaches}
print( "Anna has %(a)s apples and %(p)s peaches." %fruits_dict)
print()
