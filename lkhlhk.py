#прога 1
x = int(input ("введите x от нуля до 100: "))
if 0 <= x <=100:
    if x%3==0 and x%5==0:
        print("Fizz Buzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")

    else:
        print(x)
else:
    print("вы ввели некоректное значение")
