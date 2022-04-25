import json
import random


def encryption(in_file):
    print('---Шифруем наш файл---')
    key = generation_key()
    print(f"Ключ: {key}")
    enc_arr = []
    data = in_file.read()
    for i in data:
        enc_arr.append(key[i])
    in_file.close()
    print("---Закончили шифрование---")
    # print(enc_arr[:10])
    return enc_arr


def decryption(in_file):
    print('---Дешифруем наш файл---')
    with open('key_subst.txt', 'r') as fr:
        v2 = json.load(fr)
    decr_arr = []
    data = in_file.read()
    for i in data:
        decr_arr.append(v2.index(i))
    in_file.close()
    print("---Закончили дешифрацию---")
    # print(decr_arr[:10])
    return decr_arr


# Данный метод считывает байты файла - in_file и проверяет их с байтами файла - in_file_2
# Если идентичны, то выводится True с выводом, иначе - вывод False
def check(in_file, in_file_2):
    data = in_file.read()
    data_2 = in_file_2.read()
    if data == data_2:
        print('Полученный файл полностью идентичен исходному')
    else:
        print('Ошибка при декодировании!')
    in_file.close()


# Функция, генерирующая ключ длиной 255 символов в случайной последовательности - shuffle
def generation_key():
    key = []
    for i in range(256):
        key.append(i)
    random.shuffle(key)
    with open('key_subst.txt', 'w') as fw:
        json.dump(key, fw)
    return key


def main():
    print('Выполняем шифрование: "Подстановки"')
    b = []
    in_file = open('Vighenere.py', "rb")
    c = encryption(in_file)
    out_file = open("lab_1_1_py", "wb")
    out_file.write(bytes(c))
    out_file.close()
    in_file = open('lab_1_1_py', "rb")
    b = decryption(in_file)
    out_file = open("lab_1_2_py.py", "wb")
    out_file.write(bytes(b))
    out_file.close()
    in_file = open("Vighenere.py", "rb")
    in_file2 = open("lab_1_2_py.py", "rb")
    check(in_file, in_file2)


if __name__ == '__main__':
    main()
