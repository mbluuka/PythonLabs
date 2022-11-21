import time

start_time = time.time()

temp = open("MSKZI.txt", "r", encoding="UTF-8")
# data = temp.read()
data = '''ХБЮЖХЛЖЮЩЫБХЛЖДЛЖЗХПНЫЯЛЖЫЖЗПДЯЛГХЛЦЫПЫШИЛЮЛВХФБХЖСЛЩЫБХЗСЛЫЯЛЦРБДЛЖДЧЫПНЫГГДЛГЫМЫШДЛХЛЖЮЩЫЗСЛЦЫЭЛЩЫБХЛЖХВЮЛЭГХЫЗЫЛЩЫБДЛГЫБЫШАДЫЛПХЭЛЩПИШДЯЛДГХЛЕПХЧЩХЛЖИГИБХЛГДЖЛЧЛАГЮШИЛАДЗДПИУЛЖЫЖЗПХЛМЮЗХБХЛГДЛЗХВЛГЫЛДАХЭХБДЖСЛГЮЛАХПЗЮГДАЛГЮЛЖЗЮНАДЧ 
'''
data_2 = []
data_3 = []

for i in range(len(data)):
    data_2.append(data[i])
    data_3.append(data[i])

letter_dict = dict()
temp_array = []

for i in data:  # если символ уже содержится в списке уникальных символов, то ничего не делаем
    # Если не содержится - добавляем в список
    if i in temp_array:
        pass
    else:
        temp_array.append(i)

temp_array_2 = []  # темпоральный список для работы цикла, из него будут удаляться уже обработанные символы

for i in temp_array:  # копирование символов из первого списка во второй
    temp_array_2.append(i)
for i in temp_array:  # создание ассоциативного массива, где ключом является символ алфавита сообщения
    letter_dict[i] = 0

k = 0  # счетчик
counter = 0  # количество символа в сообщении

while len(temp_array_2) != 0:  # пока темпоральный список не пуст
    for i in data:
        if i == temp_array[k]:  # Если встречается текущий уникальный символ в сообщении, то counter прибавляет единицу
            counter += 1
    letter_dict[temp_array[k]] = counter  # символу сопоставляется его количество в сообщении
    temp_array_2.remove(temp_array[k])  # из темпорального массива удаляется уже посчитанный символ
    counter = 0  # обнуляем counter
    k += 1  # переходим на следующий символ алфавита

list_temp: list = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
letter_list_final = []
dict_final: dict = {}

for i in range(len(list_temp)):
    dict_final[list_temp[i][0]] = list_temp[i][1]
print(dict_final)
for i in dict_final:
    letter_list_final.append(i)
print(letter_list_final)

lst_letter_frequency = ["  ", 'О', 'Е', 'А', 'И', 'Н', 'Т', 'С', 'Р', 'В', 'Л', 'К', 'М', 'Д', 'П', 'У', 'Я', 'Ы', 'З',
                        'Ь', 'Б', 'Г', 'Ч', 'Й', 'Х', 'Ж', 'Ю', 'Ш', 'Ц', 'Щ', 'Э']
print(lst_letter_frequency)
print("the power of the alphabet of a given message: ", len(temp_array))
print("message length: ", len(data), "symbol's")


def generate_notepad_from_two_lists(letter_list_final: list, lst_letter_frequency: list) -> dict:
    return {k: v for v, k in zip(lst_letter_frequency, letter_list_final)}


slovar = generate_notepad_from_two_lists(letter_list_final, lst_letter_frequency)
print(slovar)
# print(data_3)

while lst_letter_frequency:  # Прямое сопоставление самых частых букв  в русском языке и в сообщении
    lst_letter_frequency.pop(0)
    for i in range(len(data_3)):
        if data_3[i] == "\n":
            pass
        elif data_3[i] == letter_list_final[0]:
            data_2[i] = slovar[letter_list_final[0]]
    letter_list_final.pop(0)

print()


def replace_letter(letter_1: str, letter_2: str):
    global data_2
    data_search = data_2
    for i in range(len(data_search)):
        if data_search[i] == letter_1:
            data_search[i] = letter_2

        elif data_search[i] == letter_2:
            data_search[i] = letter_1


flag = True
question = 0
while flag:
    for i in range(len(data_2)):
        print(data_2[i], end="")
    print()
    # question = int(input("want to quit? (1-Y;2-N)"))
    question = 2
    if question == 1:
        break
    if question == 2:
        letter_1 = str(input("letter_1 = "))
        letter_2 = str(input("letter_2 = "))
        replace_letter(letter_1, letter_2)
    if question != 2 and question != 1:
        print("Incorrect data!")
        break

print()

time = time.time() - start_time
print('running time program is ->', round(time, 4), '<- seconds')