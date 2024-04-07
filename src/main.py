keyboard_mapping = {
    'q': 'w', 'w': 'e', 'e': 'r', 'r': 't', 't': 'y', 'y': 'u', 'u': 'i', 'i': 'o', 'o': 'p',
    'a': 's', 's': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k', 'k': 'l', 'l': ';',
    'z': 'x', 'x': 'c', 'c': 'v', 'v': 'b', 'b': 'n', 'n': 'm', 'm': ',',
    'Q': 'W', 'W': 'E', 'E': 'R', 'R': 'T', 'T': 'Y', 'Y': 'U', 'U': 'I', 'I': 'O', 'O': 'P',
    'A': 'S', 'S': 'D', 'D': 'F', 'F': 'G', 'G': 'H', 'H': 'J', 'J': 'K', 'K': 'L', 'L': ':',
    'Z': 'X', 'X': 'C', 'C': 'V', 'V': 'B', 'B': 'N', 'N': 'M', 'M': '<', ' ':' ', ',':'.', '.':'/', 'p':'[', 'P':'{'
}


def encoding(key):
    value = keyboard_mapping[key]
    return value

def decoding(val):
    for key, value in keyboard_mapping.items():
        if(value == val):
            return key

encode = ''

decode = ''

while(True):
    choice  = int(input("Enter\n 1 -> For encoding\n 2 -> For decoding\n 0 -> To exit\n"))
    if(choice == 1):
        userinp = input("Enter string to encode message: ")
        for val in userinp:
             value = encoding(val)
             encode = encode+value
        print("encode value is: "+encode)
        encode= ''
    elif(choice == 2):
        userinp = input("Enter string to dencode message: ")
        for val in userinp:
             value = decoding(val)
             decode = decode+value
        print("decoded value is: "+decode)
        decode= ''
    elif(choice == 0):
        exit(0)
    else:
        print("Invalid choice")
