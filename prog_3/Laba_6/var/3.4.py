abc = "abcdefghijklmnopqrstuvwxyz"

def rot13(x):
    
    return "".join([abc[(abc.find(c)+13)%26] for c in x])
x = input("Enter word to crypt:")

print(rot13(x))
