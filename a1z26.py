import string


low = string.ascii_lowercase
upp = string.ascii_uppercase


def a1z26_enc(text: str):
    result = ''
    for letter in text:
        if letter == ' ':
            result+='0'
            result+='-'
        elif letter.islower():
            for upp_let in low:
                if letter == upp_let:
                    result+=str(low.index(letter)+1)
                    result+='-'
        elif letter.isupper():
            for upp_let in upp:
                if letter == upp_let:
                    result+=str(upp.index(letter)+1)
                    result+='-'

    return result[:-1]


def a1z26_dec(enc_text: str):
    result = ''
    enc_text = enc_text.lower()
    enc_arr = enc_text.split('-')
    new_arr = [int(i) for i in enc_arr]
    
    for num in new_arr:
        if num == 0:
            result+=' '
        for low_let in low:
            if num == low.index(low_let) + 1:
                result+=low_let
                
    return result


def main():
    text = input('Enter text -> ')
    enc = a1z26_enc(text)
    print('Encrypt : ' + enc)
    dec = a1z26_dec(enc)
    print('Decryt : ' + dec)


if __name__ == '__main__':
    main()