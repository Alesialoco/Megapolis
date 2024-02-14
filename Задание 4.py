with open("space.txt") as file:  # открытие файла
    a = [i.strip().split("*") for i in file.readlines()][1:]  # удаление первой строки и разделение по *
for i in a:
  password = i[1][-3:].upper() + (i[0][1:3].upper())[::-1] + (i[1][:3].upper())[::-1]  #создание пароля
  i.append(password)  #добавление пароля
print(a)  #вывод элементов
