import json
import random


def check(in_file, in_file_2):
    data = in_file.read()
    data_2 = in_file_2.read()
    if data == data_2:
        print('Полученный файл полностью идентичен исходному')
    else:
        print('Ошибка при декодировании!')
    in_file.close()


def generation_key(in_file):
    key = []
    data = in_file.read()
    for i in range(len(data)):
        key.append(random.randint(0, 256))
    with open('key_notebook.txt', 'w') as fw:
        json.dump(key, fw)
    print(f"Ключ длиной {len(key)} символов создан")
    return key


def encryption(in_file, key):
    print('---Шифруем наш файл---')
    enc_arr = []
    data = in_file.read()
    dt_arr = []
    for i in data:
        dt_arr.append(i)

    # print(len(dt_arr))

    i = 0
    for letter in dt_arr:
        ence = (letter ^ key[i]) % 256  # зашифрованный символ  XOR -> +
        i += 1
        enc_arr.append(ence)

    # print(enc_arr)
    print("--- Закончили шифровать ---")
    return enc_arr


def decryption(in_file):
    print("Дешифруем файл")
    with open('key_notebook.txt', 'r') as fr:
        key = json.load(fr)
    # print(f'Ключ шифрования: {key}')
    decr_arr = []
    data = in_file.read()
    i = 0
    for each_split in data:
        # print(each_split)
        ence = (each_split ^ key[i]) % 256  # зашифрованный символ  XOR -> +
        i += 1
        decr_arr.append(ence)
    print("--- Закончили дешифрацию ---")
    return decr_arr


in_file = open('5-crypto_labs.pdf', "rb")
key = generation_key(in_file)

in_file = open('5-crypto_labs.pdf', "rb")
enc = encryption(in_file, key)
out_file = open("lab_4_1", "wb")
out_file.write(bytes(enc))
out_file.close()

in_file = open("lab_4_1", "rb")
decr = decryption(in_file)
out_file = open("lab_4_2.pdf", "wb")
out_file.write(bytes(decr))
out_file.close()

in_file = open("5-crypto_labs.pdf", "rb")
in_file_2 = open("lab_4_2.pdf", "rb")
check(in_file, in_file_2)
