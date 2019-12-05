#Well, I don't know how to do md5 stuff yet... Let's learn.

import hashlib

secretKey = b'iwrupvqb'

parentHasher = hashlib.md5()

parentHasher.update(secretKey)

i = 1
while True:
    h = parentHasher.copy()
    h.update(bytes(str(i), 'utf-8'))
    if str(h.hexdigest())[:5] == '00000':
        print(i)
        break
    i += 1

