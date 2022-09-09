import sys


def encrypt(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        x = (ord(plain_text[i]) + ord(key[i])) % 26 + ord("A")
        cipher_text += chr(x)
    return cipher_text


if __name__ == "__main__":
    plain_text = sys.argv[1]
    key = sys.argv[2]
    cipher_text = encrypt(plain_text, key)
    print("Encrypted Text:", cipher_text)
