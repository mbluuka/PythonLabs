import os
import platform

import hashlib

with open ('password.txt', 'w') as write_file:
    write_file.write(hashlib.pbkdf2_hmac('sha256', 'rock'.encode(), ''.encode(), 10).hex())