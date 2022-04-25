import random, json

def encryption_1(in_file):
    print('---Шифруем наш файл---')
    v1 = generation_1()
    c = []
    data = in_file.read()
    for i in data:
        c.append(v1[i])
    in_file.close()
    return c

def decryption_1(in_file):
    print('---Дешифруем наш файл---')
    with open('file_1.txt', 'r') as fr:
        v2 = json.load(fr)
    b = []
    data = in_file.read()
    for i in data:
        b.append(v2.index(i))
    in_file.close()
    return b

def check_1(in_file,in_file2):
    data = in_file.read()
    data2 = in_file2.read()
    if data == data2:
        print('Полученный файл полностью идентичен исходному')
    else:
        print('Ошибка при декодировании!')
    in_file.close()

def generation_1():
    v1 = []
    for i in range(256):
        v1.append(i)
    random.shuffle(v1)
    with open('file_1.txt', 'w') as fw:
        json.dump(v1, fw)
    return v1

if __name__ == '__main__':
    print('Подстановки')
    b = []
    in_file = open('5-crypto_labs.pdf', "rb")
    c = encryption_1(in_file)
    out_file = open("lab_1_1", "wb")
    out_file.write(bytes(c))
    out_file.close()
    in_file = open('lab_1_1', "rb")
    b = decryption_1(in_file)
    out_file = open("lab_1_2.pdf", "wb")
    out_file.write(bytes(b))
    out_file.close()
    in_file = open("5-crypto_labs.pdf", "rb")
    in_file2 = open("lab_1_2.pdf", "rb")
    check_1(in_file,in_file2)



