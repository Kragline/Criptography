matrix = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'ij', 'k'],
    ['l', 'm', 'n', 'o', 'p'],
    ['q', 'r', 's', 't', 'u'],
    ['v', 'w', 'x', 'y', 'z']
]


def polybius_enc(item: str):
    new_text = ''
    text_arr = item.split(' ')

    for item in text_arr:
        for letter in item:
            if letter == 'i' or letter == 'j':
                new_text += 'o'
            elif letter == ' ':
                new_text += ' '
            else:
                for i in range(5):
                    for j in range(5):
                        if letter == matrix[i][j]:
                            if letter not in matrix[4]:
                                new_text += matrix[i+1][j]
                            else:
                                new_text += matrix[0][j]
        new_text += ' '
                            
    return new_text[:-1]


def polybius_dec(enc_text: str):
    new_text = ''
    enc_text_arr = enc_text.split(' ')

    for text in enc_text_arr:
        for letter in text:
            if letter == 'o':
                new_text += 'i(j)'        
            elif letter == ' ':
                new_text += ' '
            else:
                for i in range(5):
                    for j in range(5):
                        if letter == matrix[i][j]:
                            if letter not in matrix[0]:
                                new_text += matrix[i-1][j]
                            else:
                                new_text += matrix[4][j]
        new_text += ' '
                                
    return new_text[:-1]


def main():
    text = input('Enter text : ').lower()
    enc_text = polybius_enc(text)
    print('Encrypt :', enc_text)
    dec_text = polybius_dec(enc_text)
    print('Decrypt :', dec_text)


if __name__ == '__main__':
    main()