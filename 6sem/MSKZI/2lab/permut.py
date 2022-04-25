import json
import random
import time


def encryption(in_file):
    print('---Шифруем наш файл---')
    data = in_file.read()
    n, v1 = generation_key()
    c = []
    for i in range(n):
        c.append(-1)
    un = []
    final = []
    count = len(data)
    cc = 0
    while True:
        if count < n:
            for i in range(count):
                un.append(data[cc])
                cc += 1
            final += un
            break
        for i in range(len(v1)):
            un.append(data[cc])
            count -= 1
            cc += 1
        for i in range(len(un)):
            m = v1.index(i)
            c[m] = un[i]
        final += c
        c.clear()
        for i in range(n):
            c.append(-1)
        un.clear()
    in_file.close()
    print(final)
    return final


def decryption(in_file):
    print('---Дешифруем наш файл---')
    with open('key_permut.txt', 'r') as fr:
        key = json.load(fr)
    print(f'Ключ шифрования: {key}')
    n = len(key)
    b = []
    data = in_file.read()
    un = {}
    count = len(data)
    cc = 0
    while True:
        if count < n:
            for i in range(count):
                b.append(data[cc])
                cc += 1
            break
        for i in key:
            un[i] = data[cc]
            count -= 1
            cc += 1
        list_keys = list(un.keys())
        list_keys.sort()
        for i in list_keys:
            b.append(un[i])
        un.clear()
    in_file.close()
    return b


def check(in_file, in_file2):
    data = in_file.read()
    data2 = in_file2.read()
    if data == data2:
        print('Полученный файл полностью идентичен исходному')
    else:
        print('Ошибка при декодировании!')
    in_file.close()


def generation_key():
    v1 = []
    n = random.randint(2, 50)
    for i in range(n):
        v1.append(i)
    random.shuffle(v1)
    with open('key_permut.txt', 'w') as fw:
        json.dump(v1, fw)
    return n, v1


if __name__ == '__main__':
    print('Перестановки')
    b = []
    in_file = open('5-crypto_labs.pdf', "rb")
    t = time.time()
    final = encryption(in_file)
    print('Время шифрования:', time.time()-t)
    out_file = open("lab_2_1", "wb")
    out_file.write(bytes(final))
    out_file.close()
    t = time.time()
    in_file = open("lab_2_1", "rb")
    b = decryption(in_file)
    print('Время дешифрования:', time.time()-t)
    out_file = open("lab_2_2.pdf", "wb")
    out_file.write(bytes(b))
    out_file.close()
    in_file = open("5-crypto_labs.pdf", "rb")
    in_file2 = open("lab_2_2.pdf", "rb")
    check(in_file, in_file2)
