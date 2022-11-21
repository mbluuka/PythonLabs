import hashlib

login = "ADMIN".encode()
password = '1234'.encode()

dk = hashlib.pbkdf2_hmac('sha256', login, password, 100000)
rock = dk.hex()
print(rock)
with open('D:/Учеба/4 курс/7 семестр/ПАСЗИ/Sertificate.txt', 'w') as write_file:
    write_file.write(f"{rock}")


with open('D:/Учеба/4 курс/7 семестр/ПАСЗИ/Sertificate.txt', 'r') as read_file:
    tmp = read_file.read()

if tmp == str(rock):
    print('okrkr')
