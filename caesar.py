def caeser_enc(text: str, key: str):
	result = ''
	all = ''
	text_arr = text.split(' ')

	for word in text_arr:
		for i in range(len(word)):
			char = word[i]
			if (char.isupper()):
				result += chr((ord(char) + key-65) % 26 + 65)
			else:
				result += chr((ord(char) + key-97) % 26 + 97)
		all += result + ' '
		result = ''

	return all[:-1]


def caeser_dec(text: str, key: str):
	result = ''
	all = ''
	text_arr = text.split(' ')

	for word in text_arr:
		for i in range(len(word)):
			char = word[i]
			if (char.isupper()):
				result += chr((ord(char) - key-65) % 26 + 65)
			else:
				result += chr((ord(char) - key-97) % 26 + 97)
		all += result + ' '
		result = ''

	return all[:-1]


def caeser_dec_without_key(text: str):
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


def main():
	text = input('Enter text -> ')
	while True:
		try:
			key = int(input('Enter key (must be int) -> '))
			break
		except ValueError:
			print('Key must be integer')

	dec = caeser_enc(text, key)
	print('Encrypted :', dec)
	enc = caeser_dec(dec, key)
	print('Decrypted :', enc)


if __name__ == '__main__':
    main()