# we will use simple ord() and chr() function to create a simple encryption
# decryption program


msg = input('Enter your message-> ')
def encrypt(msg):
    encrypt_msg = ''
    for x in msg:
        encrypt_msg += chr(ord(x) + 1)
    return encrypt_msg


def decrypt(msg):
    decrypt_msg = ''
    for x in msg:
        decrypt_msg += chr(ord(x) - 1)
    return decrypt_msg


enc_dec = input('Do you want to encrypt it or decrypt it (E/D) ').lower()
if enc_dec == 'e':
    print('the encrypted message-> ' + encrypt(msg))
else:
    print('the decrypted message is-> '+decrypt(msg))
