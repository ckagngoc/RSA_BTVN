#file name : RSA_btvn.py
#author: Pham Duc Minh

import math
import random as rd
from Crypto.PublicKey import RSA

plaintext = 'Ask questions. Never stop learning. Do not pay attention to what others think of you.\
    Read everyday. Study hard. Teach others what you know. Make mistakes and learn.'
#e =  25
e = 25
#p =  8764541117
p = 8764541117
#q =  9699423919
q = 9699423919
n = p * q
T = (p - 1) * (q - 1)
d = pow(e,-1,T)
print('e = ',e)
print('p = ',p)
print('q = ',q)
print('n = ',n)
print('T = ',T)
print('d = ',d)

#Kiểm tra số Nguyên Tố
'''def checkNT(num):
    if(type(num) != int):
        return False
    for x in range(2,int(math.sqrt(num)) + 1):
        if ((num % x) == 0):
            return False
    return True'''

def encrypt(text):
    #Sinh dữ liệu mã hóa
    '''e =  25
    print('e = ',e)

    p = q = 0
    while(p == 0 & q == 0):
        a = rd.randint(1e6, 1e10)
        b = rd.randint(1e6, 1e10)
        T = (a - 1) * (b - 1)
        if(checkNT(a) and checkNT(b) and math.gcd(e, T) == 1):
            p = a
            q = b
    n = p * q
    T = (p - 1) * (q - 1)       
    d = pow(e,-1,T)
    print('p = ',p)
    print('q = ',q)
    print('n = ',n)
    print('T = ',T)
    print('d = ',d)'''
    lsPlainText = [ord(x) for x in text]
    lsCipherText = []
    print('lsPlainText = ',lsPlainText)
    f = open('encryption.txt','w')
    for x in lsPlainText:
        c = (x**e) % n
        lsCipherText.append(c)
        f.write(str(int(c)) + ' ')
    f.close()
    print('lsCipherText = ',lsCipherText)

#Decryption
'''def decrypt():
    f = open('encryption.txt','r')
    f2 = open('decryption.txt','w')
    text = f.read()
    f.close()
    ls = [int(x) for x in text.strip(' ').split(' ')]
    for x in ls:
        c = (x**d) % n
        f2.write(chr(c))
    f2.close()'''

encrypt(plaintext)
#decrypt()
