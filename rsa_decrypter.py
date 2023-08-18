

import rsa

"""#decrypting


"""

#reading private_key text file
try:
  f = open('priv.txt', 'r')
  priv = f.read()
  f.close()
except:
  print('private key file not found. please keep the priv.txt file in the same directory and try again')
key = rsa.PrivateKey.load_pkcs1(priv)

#you can use it to read message. bin
try:
  f = open('message.bin', 'rb')
  enc_msg = f.read()
  f.close()
except:
  print('encrypted message.bin file not found')
  f.close()

enc_msg = b"c\xe7\xfax\x0bB\xa4Z\xc9\xee\x9c\xecL\t\xa4\xc7u\xe2o\xc7\x94\xe4L\x06\xcc\x13\xce\xb7\xa2\x91\xca\xd5\x02\x96\x8a)\xca\x87\xb7\x825a\xb9\xeb\xc7^\x0f\x07\xc8O\x02D\x8e\xb9\xb6\x9d'\n\x1c\x80qI\xee\x1e"

"""#decoding"""

key = rsa.PrivateKey.load_pkcs1(priv)

dec_msg = rsa.decrypt(enc_msg, key).decode()
dec_msg