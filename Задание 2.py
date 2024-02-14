with open("space.txt") as file:  # открытие файла
    a = [i.strip().split("*")[0] for i in file.readlines()][1:]  # удаление первой строки и разделение по *
for i in range(len(a)):  #сортировка пузырьком
    for j in range(len(a)):
        if i != j:
            if int(a[i][5:]) < int(a[j][5:]):   #сравнение двух элементов
                a[i], a[j] = a[j], a[i]    #если необходимо, изменение мест элементов
print(a[:10])   #вывод первых десяти кораблей
