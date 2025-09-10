def razmen(summa, nominaly):
    nominaly.sort(reverse=True)
    result = {}
    for nominal in nominaly:
        result[nominal] = 0
    ostalos = summa
    for nominal in nominaly:
        while ostalos >= nominal:
            ostalos -= nominal
            result[nominal] += 1
    if ostalos == 0:
        return result
    else:
        return "-42!"
try:
    summa = int(input("Введите сумму для размена: "))
    if summa < 0:
      print("Сумма должна быть неотрицательной.")
    else:
      nominaly = [9, 7, 10]
      result = razmen(summa, nominaly)
      print(result)
except ValueError:
    print("Ошибка: Введите целое число для суммы.")