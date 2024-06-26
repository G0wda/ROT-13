import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", type=str,required=False,default="")
args = parser.parse_args()

def rot13_translator():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    shift = 13

    shift_lowercase = lowercase[shift:] + lowercase[:shift]
    shift_uppercase = uppercase[shift:] + uppercase[:shift]

    translate = str.maketrans(lowercase + uppercase , shift_lowercase + shift_uppercase)
    return translate

def rot13(message):
    table = rot13_translator()
    return message.translate(table)

if args.filepath:
    fpath = args.filepath
    fopen  = open(fpath, 'r')
    reader  = fopen.readlines()
    msg = ''.join(reader)
    cipher = rot13(msg)

    print("Cipher text: ", cipher)
    exit

else:
    input_message = input("Enter message: ")

    cipher = rot13(input_message)
    print("Encrypted cipher is: ",cipher)

    decipher  = rot13(cipher)
    print("Decrypted cipher: ",decipher)




