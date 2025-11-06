a = input(int("enter first number: "))
b = input(int("enter second number: "))
op = input("enter operator +, -, *, / :")
if op == "+":
    print(a+b)
elif op == "=":
    print(a-b)
elif op == "*":
    print(a*b)
else:
    print(a/b)