#прога 2
a=int(input("введите число: "))
b=int(input("введите степень от 0 до 7: "))
if 0<=b<=7:
    print(a**b)
else:
    print("error")