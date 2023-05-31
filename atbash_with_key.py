import string as st


def atbash_with_key(text: str, key: str):
    new_str = st.ascii_lowercase[::-1]
    new_lower_alp = key
    
    for char in new_str:
        if char not in new_lower_alp:
            new_lower_alp+=char
            
    lower = dict(zip(st.ascii_lowercase, new_lower_alp))
    changed = ''

    for letter in text:
        for symbol in lower:
            if letter == symbol:
                changed += lower[symbol]
    
    return changed
    

def main():
    text = input('Enter text -> ').lower()
    key = input('Enter key -> ').lower()
    print('Encrypted text :', atbash_with_key(text, key))


if __name__ == '__main__':
    main()