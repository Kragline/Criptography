dictionary = {
    'a': '01000001',
    'b': '01000010',
    'c': '01000011',
    'd': '01000100',
    'e': '01000101',
    'f': '01000110',
    'g': '01000111',
    'h': '01001000',
    'i': '01001001',
    'j': '01001010',
    'k': '01001011',
    'l': '01001100',
    'm': '01001101',
    'n': '01001110',
    'o': '01001111',
    'p': '01010000',
    'q': '01010001',
    'r': '01010010',
    's': '01010011',
    't': '01010100',
    'u': '01010101',
    'v': '01010110',
    'w': '01010111',
    'x': '01011000',
    'y': '01011001',
    'z': '01011010'
}


def make_same_length(text: str, key: str):
    new_key = ''
    while True:
        if len(new_key) + len(key) < len(text):
            new_key += key
        else:
            break

    if len(new_key) < len(text):
        length = len(text) - len(new_key)
        new_key += new_key[:length]

    return new_key


def xor_enc(text: str, key: str):
    changed_t = ''
    changed_k = ''
    changed = ''

    for letter in text:
        for symbol in dictionary:
            if letter == symbol:
                changed_t += dictionary[symbol]

    for letter in key:
        for symbol in dictionary:
            if letter == symbol:
                changed_k += dictionary[symbol]

    for i in range(len(changed_t)):
        if changed_t[i] == '0' and changed_k[i] == '0' or changed_t[i] == '1' and changed_k[i] == '1':
            changed += '0'
        else:
            changed += '1'

    return changed


def xor_dec(enc_text: str, key: str):
    changed_k = ''
    text = ''
    final = ''

    for letter in key:
        for symbol in dictionary:
            if letter == symbol:
                changed_k += dictionary[symbol]

    for i in range(len(changed_k)):
        if enc_text[i] == '0' and changed_k[i] == '0' or enc_text[i] == '1' and changed_k[i] == '1':
            text += '0'
        else:
            text += '1'

    diapasone = 8
    output_nums = [(text[i:i+diapasone]) for i in range(0, len(text), diapasone)]
        
    for num in output_nums:
        for sym in dictionary:
            if num == dictionary[sym]:
                final += sym

    return final


def main():
    text = input('Enter text -> ').lower()
    key = input('Enter key -> ').lower()

    if len(text) > len(key):
        key = make_same_length(text, key)

    enc_text = xor_enc(text, key)
    print('Encrypt :', enc_text)
    dec_text = xor_dec(enc_text, key)
    print('Decrypt :', dec_text)
    


if __name__ == '__main__':
    main()