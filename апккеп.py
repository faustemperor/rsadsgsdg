#прога 3
print("стоимость разговора")
x= input("введите название вашего оператора: ")
y= input("введите название другого оператора: ")
if x == ("Билайн"):
    if y == "Билайн":
        print("стоимость 0")
    elif y == "МТС":
        print("стоимость 20")
    elif y == "Теле2":
        print("стоимость 20")
    elif y == "Мегафон":
        print("стоимость 20")
    else:
        print("оператор не найден")
elif x == ("МТС"):
    if y == "Билайн":
        print("стоимость 15")
    elif y == "МТС":
        print("стоимость 0")
    elif y == "Теле2":
        print("стоимость 15")
    elif y == "Мегафон":
        print("стоимость 15")
    else:
        print("оператор не найден")
elif x == ("Теле2"):
    if y == "Билайн":
        print("стоимость 12")
    elif y == "МТС":
        print("стоимость 12")
    elif y == "Теле2":
        print("стоимость 0")
    elif y == "Мегафон":
        print("стоимость 12")
    else:
        print("оператор не найден")
elif x == ("Мегафон"):
    if y == "Билайн":
        print("стоимость 17")
    elif y == "МТС":
        print("стоимость 17")
    elif y == "Теле2":
        print("стоимость 17")
    elif y == "Мегафон":
        print("стоимость 0")
    else:
        print("оператор не найден")
else:
    print("оператор не найден")