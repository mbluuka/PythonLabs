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


def generation_key():
    key = []
    for i in range(256):
        key.append(random.randint(0, 256))
    # random.shuffle(key)
    with open('key_vighen.txt', 'w') as fw:
        json.dump(key, fw)
    return key


def encryption(in_file):
    print('---Шифруем наш файл---')
    key = generation_key()
    print(f"Ключ: {key} \nC длиной: {len(key)} символов")
    enc_arr = []
    data = in_file.read()
    split_data = [data[i:i + len(key)] for i in range(0, len(data), len(key))]
    for each_split in split_data:
        i = 0
        for letter in each_split:  # letter - int
            ence = (letter + key[i]) % len(key)  # зашифрованный символ  XOR -> +
            i += 1
            enc_arr.append(ence)
    # print(enc_arr)
    return enc_arr


def decryption(in_file):
    print("Дешифруем файл")
    with open('key_vighen.txt', 'r') as fr:
        key = json.load(fr)
    print(f'Ключ шифрования: {key}')
    decr_arr = []
    data = in_file.read()
    split_data = [data[i:i + len(key)] for i in range(0, len(data), len(key))]
    for each_split in split_data:
        i = 0
        for letter in each_split:  # letter - int
            ence = (letter - key[i]) % len(key)  # зашифрованный символ  XOR -> +
            i += 1
            decr_arr.append(ence)
    # print(enc_arr)
    return decr_arr


in_file = open('5-crypto_labs.pdf', "rb")
enc = encryption(in_file)
out_file = open("lab_3_1", "wb")
out_file.write(bytes(enc))
out_file.close()

in_file = open("lab_3_1", "rb")
decr = decryption(in_file)
out_file = open("lab_3_2.pdf", "wb")
out_file.write(bytes(decr))
out_file.close()

in_file = open("5-crypto_labs.pdf", "rb")
in_file_2 = open("lab_3_2.pdf", "rb")
check(in_file, in_file_2)
