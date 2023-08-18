

import rsa

"""#Generating Keys"""

def generatekeys():
  public_key, private_key = rsa.newkeys(512)
  priv = private_key.save_pkcs1().decode('utf-8')
  pub = public_key.save_pkcs1().decode('utf-8')
  f = open('priv.txt', 'w')
  f.write(priv)
  f.close()

  f = open('pub.txt', 'w')
  f.write(pub)
  f.close()
  return public_key, private_key

while(1):
  x_inp = input('do you have existing key files priv.txt and pub.txt (y/n): ')
  if x_inp == 'n':
    public_key, private_key = generatekeys()
    print('keys generated')
    break
  elif x_inp == 'y':
    try:
      f = open('pub.txt', 'r')
      pub = f.read()
      f.close()
    except:
      print('key file does not exist. please press n when prompted to generate key files')
      continue
    public_key = rsa.PublicKey.load_pkcs1(pub)
    print('public key loaded from existing file')
    break
  else:
    print('wrong input please try again')

"""#User Input"""

msg = "this is a dummy secret message"
msg = input('enter text you want to encrypt: ')

"""#Encrypting

"""

enc_msg = rsa.encrypt(msg.encode(), public_key)
f = open('message.bin', 'wb')
f.write(enc_msg)
f.close()
print('encrypted message: ', enc_msg)
print('the message is encrypted and saved in message.bin file')

"""#decoding"""

f = open('message.bin', 'rb')
enc_msg = f.read()
f.close()

f = open('priv.txt', 'r')
priv = f.read()
f.close()

key = rsa.PrivateKey.load_pkcs1(priv)

dec_msg = rsa.decrypt(enc_msg, key).decode()
dec_msg