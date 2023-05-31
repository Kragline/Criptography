import string


lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase


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

    
def encrypt(text: str, key: str):
    final_text = ''
    i_text = 0
    i_key = 0

    for _ in range(len(text)):
        text_letter = text[i_text]
        key_letter = key[i_key]
        new_text_index = 0
        new_key_index = 0

        if text_letter.isupper():
            for i in range(len(upper_alphabet)):
                if text_letter == upper_alphabet[i]:
                    new_text_index = i
                if key_letter == lower_alphabet[i]:
                    new_key_index = i
            final_text += upper_alphabet[(new_text_index+new_key_index) % len(upper_alphabet)]
            i_key+=1
            i_text+=1
        elif text_letter.islower():
            for i in range(len(lower_alphabet)):
                if text_letter == lower_alphabet[i]:
                    new_text_index = i
                if key_letter == lower_alphabet[i]:
                    new_key_index = i
            final_text += lower_alphabet[(new_text_index+new_key_index) % len(lower_alphabet)]
            i_key+=1
            i_text+=1
        elif text_letter == ' ':
            final_text += ' '
            i_text+=1

    return final_text


def decrypt(enc_text: str, key: str):
    final_text = ''
    i_text = 0
    i_key = 0

    for _ in range(len(enc_text)):
        enc_text_letter = enc_text[i_text]
        key_letter = key[i_key]
        new_text_index = 0
        new_key_index = 0

        if enc_text_letter.isupper():
            for i in range(len(upper_alphabet)):
                if enc_text_letter == upper_alphabet[i]:
                    new_text_index = i
                if key_letter == lower_alphabet[i]:
                    new_key_index = i
            final_text += upper_alphabet[(new_text_index-new_key_index) % len(upper_alphabet)]
            i_key+=1
            i_text+=1
        elif enc_text_letter.islower():
            for i in range(len(lower_alphabet)):
                if enc_text_letter == lower_alphabet[i]:
                    new_text_index = i
                if key_letter == lower_alphabet[i]:
                    new_key_index = i
            final_text += lower_alphabet[(new_text_index-new_key_index) % len(lower_alphabet)]
            i_key+=1
            i_text+=1
        elif enc_text_letter == ' ':
            final_text += ' '
            i_text+=1

    return final_text


def main():
    text = input('Type text to encrypt -> ')
    key = input('Enter key -> ').lower()

    if len(text) > len(key):
        key = make_same_length(text, key)
        print('New key : ' + key + '\n')

    encrypted_text = encrypt(text, key)
    print('Encrypted : ' + encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print('Decrypted : ' + decrypted_text)


if __name__ == '__main__':
    main()