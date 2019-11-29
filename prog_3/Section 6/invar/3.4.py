abc = "abcdefghijklmnopqrstuvwxyz"

def crypt_13(x):

    return "".join([abc[(abc.find(c)+13)%26] for c in x])
x = input("Enter word to crypt:")

print(crypt_13(x))
