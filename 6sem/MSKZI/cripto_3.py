import cripto_1, cripto_2


def encryption_3_1(in_file,out_file):
    print('Шифруем подстановкой')
    c = cripto_1.encryption_1(in_file)
    out_file.write(bytes(c))
    out_file.close()
    print()


def encryption_3_2(in_file,out_file):
    print('Шифруем перестановкой')
    final = cripto_2.encryption_2(in_file)
    out_file.write(bytes(final))
    out_file.close()
    print()


def decryption_3_1(in_file,out_file):
    print('Дешифруем перестановкой')
    b = cripto_2.decryption_2(in_file)
    out_file.write(bytes(b))
    out_file.close()
    print()


def decryption_3_2(in_file,out_file):
    print('Дешифруем подстановкой')
    b = cripto_1.decryption_1(in_file)
    out_file.write(bytes(b))
    out_file.close()
    print()


def check_3(in_file, in_file2):
    print('Проверка:')
    cripto_2.check_2(in_file, in_file2)
    print()


if __name__ == '__main__':
    in_file = open('server.exe', "rb")
    out_file = open("lab_3_1", "wb")
    encryption_3_1(in_file, out_file)
    in_file = open('lab_3_1', "rb")
    out_file = open("lab_3_2", "wb")
    encryption_3_2(in_file, out_file)
    in_file = open("lab_3_2", "rb")
    out_file = open("lab_3_3", "wb")
    decryption_3_1(in_file, out_file)
    in_file = open('lab_3_1', "rb")
    in_file2 = open("lab_3_3", "rb")
    check_3(in_file, in_file2)
    in_file = open('lab_3_3', "rb")
    out_file = open("lab_3_4.exe", "wb")
    decryption_3_2(in_file, out_file)
    in_file = open("server.exe", "rb")
    in_file2 = open("lab_3_4.exe", "rb")
    check_3(in_file, in_file2)
