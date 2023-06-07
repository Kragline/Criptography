import string


class Criptography:

    def __init__(self) -> None:
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        
        self.lower_for_atbash = dict(zip(self.lowercase + ' ', self.lowercase[::-1] + ' '))
        self.upper_for_atbash = dict(zip(self.uppercase, self.lowercase[::-1]))

        self.polybius_matrix = [
            ['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'ij', 'k'],
            ['l', 'm', 'n', 'o', 'p'],
            ['q', 'r', 's', 't', 'u'],
            ['v', 'w', 'x', 'y', 'z']
        ]

        self.xor_dictionary = {
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

    def a1z26_encrypt(self, text: str):
        result = ''
        for letter in text:
            if letter == ' ':
                result+='0'
                result+='-'
            elif letter.islower():
                for upp_let in self.lowercase:
                    if letter == upp_let:
                        result+=str(self.lowercase.index(letter)+1)
                        result+='-'
            elif letter.isupper():
                for upp_let in self.uppercase:
                    if letter == upp_let:
                        result+=str(self.uppercase.index(letter)+1)
                        result+='-'

        return result[:-1]
    
    def a1z26_decrypt(self, enc_text: str):
        result = ''
        enc_text = enc_text.lower()
        enc_arr = enc_text.split('-')
        new_arr = [int(i) for i in enc_arr]
        
        for num in new_arr:
            if num == 0:
                result+=' '
            for low_let in self.lowercase:
                if num == self.lowercase.index(low_let) + 1:
                    result+=low_let
                    
        return result
    
    def atbash_with_key(self, text: str, key: str):
        new_str = self.lowercase[::-1]
        new_lower_alp = key
        
        for char in new_str:
            if char not in new_lower_alp:
                new_lower_alp+=char
                
        lower = dict(zip(self.lowercase, new_lower_alp))
        changed = ''

        for letter in text:
            for symbol in lower:
                if letter == symbol:
                    changed += lower[symbol]
        
        return changed

    def atbash_encrypt(self, text: str):
        changed = ''

        for letter in text:
            if letter.isupper():
                for symbol in self.upper_for_atbash:
                    if letter == symbol:
                        changed += self.upper_for_atbash[symbol]
            else:
                for symbol in self.lower_for_atbash:
                    if letter == symbol:
                        changed += self.lower_for_atbash[symbol]
        
        return changed
    
    def caeser_encrypt(self, text: str, key: int):
        result = ''
        all = ''
        text_arr = text.split(' ')

        for word in text_arr:
            for i in range(len(word)):
                char = word[i]
                if char.isupper():
                    result += chr((ord(char) + key-65) % 26 + 65)
                else:
                    result += chr((ord(char) + key-97) % 26 + 97)
            all += result + ' '
            result = ''

        return all[:-1]
    
    def caeser_decrypt(self, text: str, key: int):
        result = ''
        all = ''
        text_arr = text.split(' ')

        for word in text_arr:
            for i in range(len(word)):
                char = word[i]
                if char.isupper():
                    result += chr((ord(char) - key-65) % 26 + 65)
                else:
                    result += chr((ord(char) - key-97) % 26 + 97)
            all += result + ' '
            result = ''

        return all[:-1]
    
    def caeser_dec_without_key(self, text: str):
        key = 1
        result = ''
        text_arr = text.split(' ')

        while key<=26:
            for word in text_arr:
                for i in range(len(word)):
                    char = word[i]
                    if (char.isupper()):
                        result += chr((ord(char) - key-65) % 26 + 65)
                    else:
                        result += chr((ord(char) - key-97) % 26 + 97)
                result += ' '
            print(f'Key is {key}: ' + result[:-1])
            key+=1
            result = ''

    def polybius_encrypt(self, item: str):
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
                            if letter == self.polybius_matrix[i][j]:
                                if letter not in self.polybius_matrix[4]:
                                    new_text += self.polybius_matrix[i+1][j]
                                else:
                                    new_text += self.polybius_matrix[0][j]
            new_text += ' '
                                
        return new_text[:-1]
    
    def polybius_decrypt(self, enc_text: str):
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
                            if letter == self.polybius_matrix[i][j]:
                                if letter not in self.polybius_matrix[0]:
                                    new_text += self.polybius_matrix[i-1][j]
                                else:
                                    new_text += self.polybius_matrix[4][j]
            new_text += ' '
                                    
        return new_text[:-1]
    
    def make_same_length(self, text: str, key: str):
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
    
    def vegenere_encrypt(self, text: str, key: str):
        final_text = ''
        i_text = 0
        i_key = 0

        if len(text) > len(key):
            key = self.make_same_length(text, key)

        for _ in range(len(text)):
            text_letter = text[i_text]
            key_letter = key[i_key]
            new_text_index = 0
            new_key_index = 0

            if text_letter.isupper():
                for i in range(len(self.uppercase)):
                    if text_letter == self.uppercase[i]:
                        new_text_index = i
                    if key_letter == self.lowercase[i]:
                        new_key_index = i
                final_text += self.uppercase[(new_text_index+new_key_index) % len(self.uppercase)]
                i_key+=1
                i_text+=1
            elif text_letter.islower():
                for i in range(len(self.lowercase)):
                    if text_letter == self.lowercase[i]:
                        new_text_index = i
                    if key_letter == self.lowercase[i]:
                        new_key_index = i
                final_text += self.lowercase[(new_text_index+new_key_index) % len(self.lowercase)]
                i_key+=1
                i_text+=1
            elif text_letter == ' ':
                final_text += ' '
                i_text+=1

        return final_text
    
    def vegenere_decrypt(self, enc_text: str, key: str):
        final_text = ''
        i_text = 0
        i_key = 0

        if len(enc_text) > len(key):
            key = self.make_same_length(enc_text, key)

        for _ in range(len(enc_text)):
            enc_text_letter = enc_text[i_text]
            key_letter = key[i_key]
            new_text_index = 0
            new_key_index = 0

            if enc_text_letter.isupper():
                for i in range(len(self.uppercase)):
                    if enc_text_letter == self.uppercase[i]:
                        new_text_index = i
                    if key_letter == self.lowercase[i]:
                        new_key_index = i
                final_text += self.uppercase[(new_text_index-new_key_index) % len(self.uppercase)]
                i_key+=1
                i_text+=1
            elif enc_text_letter.islower():
                for i in range(len(self.lowercase)):
                    if enc_text_letter == self.lowercase[i]:
                        new_text_index = i
                    if key_letter == self.lowercase[i]:
                        new_key_index = i
                final_text += self.lowercase[(new_text_index-new_key_index) % len(self.lowercase)]
                i_key+=1
                i_text+=1
            elif enc_text_letter == ' ':
                final_text += ' '
                i_text+=1

        return final_text
    
    def xor_encrypt(self, text: str, key: str):
        changed_t = ''
        changed_k = ''
        changed = ''

        if len(text) > len(key):
            key = self.make_same_length(text, key)

        for letter in text:
            for symbol in self.xor_dictionary:
                if letter == symbol:
                    changed_t += self.xor_dictionary[symbol]

        for letter in key:
            for symbol in self.xor_dictionary:
                if letter == symbol:
                    changed_k += self.xor_dictionary[symbol]

        for i in range(len(changed_t)):
            if changed_t[i] == '0' and changed_k[i] == '0' or changed_t[i] == '1' and changed_k[i] == '1':
                changed += '0'
            else:
                changed += '1'

        return changed
        
    def xor_decrypt(self, enc_text: str, key: str):
        changed_k = ''
        text = ''
        final = ''

        for letter in key:
            for symbol in self.xor_dictionary:
                if letter == symbol:
                    changed_k += self.xor_dictionary[symbol]

        for i in range(len(changed_k)):
            if enc_text[i] == '0' and changed_k[i] == '0' or enc_text[i] == '1' and changed_k[i] == '1':
                text += '0'
            else:
                text += '1'

        diapasone = 8
        output_nums = [(text[i:i+diapasone]) for i in range(0, len(text), diapasone)]
            
        for num in output_nums:
            for sym in self.xor_dictionary:
                if num == self.xor_dictionary[sym]:
                    final += sym

        return final