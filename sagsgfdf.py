#прога 4
def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission = sales * 0.03
    elif sales <= 1000:
        commission = sales * 0.05
    else:
        commission = sales * 0.08
    return base_salary + commission

sales_manager_1 = float(input("Введите уровень продаж для менеджера 1: "))
sales_manager_2 = float(input("Введите уровень продаж для менеджера 2: "))
sales_manager_3 = float(input("Введите уровень продаж для менеджера 3: "))

salary_manager_1 = calculate_salary(sales_manager_1)
salary_manager_2 = calculate_salary(sales_manager_2)
salary_manager_3 = calculate_salary(sales_manager_3)

print(f"Зарплата менеджера 1: ${salary_manager_1:.2f}")
print(f"Зарплата менеджера 2: ${salary_manager_2:.2f}")
print(f"Зарплата менеджера 3: ${salary_manager_3:.2f}")

salaries = [salary_manager_1, salary_manager_2, salary_manager_3]
best_manager_index = salaries.index(max(salaries))

salaries[best_manager_index] += 200

print(f"Лучший менеджер: Менеджер {best_manager_index + 1} с зарплатой ${salaries[best_manager_index]:.2f}")