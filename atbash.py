import string as st


upper = dict(zip(st.ascii_uppercase, st.ascii_lowercase[::-1]))
lower = dict(zip(st.ascii_lowercase + ' ', st.ascii_lowercase[::-1] + ' '))


def atbash_enc(text: str):
    changed = ''

    for letter in text:
        if letter.isupper():
            for symbol in upper:
                if letter == symbol:
                    changed += upper[symbol]
        else:
            for symbol in lower:
                if letter == symbol:
                    changed += lower[symbol]
    
    return changed


def main():
    text = input('Enter text -> ')
    print('Encrypted text : ', atbash_enc(text))


if __name__ == '__main__':
    main()