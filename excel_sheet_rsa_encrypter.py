

import rsa
import pandas as pd
import numpy as np

"""#loading dataframe"""

df = pd.read_excel('dummy.xlsx')

df

df.tail(1)

df['enc_pass'] = "NA"
df

"""#Generating Keys"""

publicKey, privateKey = rsa.newkeys(512)

priv = privateKey.save_pkcs1().decode('utf-8')
pub = publicKey.save_pkcs1().decode('utf-8')

f = open('priv-key.txt', 'w')
f.write(priv)
f.close()

f = open('pub-key.txt', 'w')
f.write(pub)
f.close()

"""#Encrypting"""

for i in range(len(df['password'])):
  if df['enc_pass'][i] == "NA":
    msg = df['password'][i]
    enc_msg = rsa.encrypt(msg.encode(), publicKey)
    df.at[i,'enc_pass'] = enc_msg

df

df = df.drop('password', axis=1)

df

df.to_excel('dummy-encrypted.xlsx', index=False)

# f = open('message.bin', 'wb')
# f.write(enc_msg)
# f.close()

"""#Decrypting"""

enc_msg = b"\xbb\xea@pa\x95\x1c\x91\xcb'q\xbc\xfa\xca\xc2jU\xda\xa6\x7f!\xc4\xe9<\xf4(\xfc.`\x00y\x94#'9\x0e*\xb9\xf1\x08\xe0\x05\x9fw\xad\xb3\xabLI\xf4\xbf\xd3@A\xf1w\xf1K\xdaM\xa5\xd90\xea"

# f = open('message.bin', 'rb')
# enc_msg = f.read()
# f.close()

f = open('priv-key.txt', 'r')
priv = f.read()
f.close()

key = rsa.PrivateKey.load_pkcs1(priv)

dec_msg = rsa.decrypt(enc_msg, key).decode()
dec_msg