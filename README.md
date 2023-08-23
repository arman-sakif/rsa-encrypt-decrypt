# rsa-encrypt-decrypt
Simple python encryption and decryption code. Both in .py file and .ipynb files. 

Dependencies:
1) python pandas
2) [rsa]([url](https://pypi.org/project/rsa/)https://pypi.org/project/rsa/)

#**How to use**
note: it is recommended that to run this in google colab, otherwise use jupyter notebook to run the ipynb files locally. It is also possible to use the .py files but that would take some experience with using python. 

1) Please ensure you have pandas and rsa installed on your system (or in the virtual environment if you want).
2) Have and 'dummy.xlsx' xcell file where one column is 'password'. Also, make sure there are no column 'enc_pass'
3) Runninng the 'xcell_sheet_rsa_encrypter' for xcell will generate 'dummy-encrypted.xlsx' and 'priv.txt' files. Please do keep the priv.txt file as this will be necessary to decrypt.
4) at the end of the 'xcell_sheet_rsa_encrypter', there's a section for decryption. And example is given there. Replace the example string by copy pasting the encrypted message in the variable 'enc_msg'. Then run the below codes and the message will be decrypted (please note that the exact priv.txt key file will be needed) .


note: this system is intended to be used once. It is not possible to modify or add. You have to encrypt a new xcell file. 


