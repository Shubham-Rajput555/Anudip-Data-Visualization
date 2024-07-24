#EXCEPTION HANDLING USING TRY AND EXPECT
a=int(input("ENTER A NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))
try:
    div=a/b
    print(div)
    print("INSIDE TRY AND EXPECT")
except ZeroDivisionError as e:
    print(e)
#EXCEPTION HANDLING USING TRY AND MULTIPLE EXPECT
a=int(input("ENTER A NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))
try:
    div=a/b
    print(div)
    open("anudip.txt")
    print("INSIDE TRY AND EXPECT")
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError as f:
    print("file nhi mil rahi")
#ELSE BLOCK
else:
    print("ELSE BLOCK")
#FINALLY BLOCK
finally:
    print("FINALLY BLOCK")
print("OUTSIDE TRY AND EXPECT")