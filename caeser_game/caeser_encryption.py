from logo_caeser import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt():
    original_text = input("enter the text to encrypt: ").strip()
    shift_amount = int(input("Enter the shift amount: "))
    result = ""
    for i in original_text:
        if i not in alphabet:
            result += i
        else:
            x = alphabet.index(i) # x is the position of the given letter in text
            i = alphabet[(x + shift_amount) % len(alphabet)] #here we update the value of ~i~ to the shifted letter 
            result += i #here i used concatenation of strings to append new new letters
    print(f"the encrypted text is: {result}")
def decrypt():
    original_text= input("enter the text to decrypt: ").strip()
    shift_number = int(input("enter the number from which is shifted: "))
    result=""
    for i in original_text:
        if i not in alphabet:
            result += i
        else:

            x = alphabet.index(i)
            i = alphabet[(x - shift_number) % len(alphabet)]
            result += i
    print(f"decrypted text is: {result}")

def caeser():
    direction = input("You wish to encode or decode? ").lower()
    if direction == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
    else:
        print("select a valid option")

caeser()
wish = input("Do you wish to continue? y/n ")
while wish == "y":
    caeser()
    wish = input("Do you wish to continue? y/n ")
else:
    print("Goodbye :3")
    exit()
