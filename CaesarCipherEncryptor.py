'''
    Caesar Cipher Encryptor:
    Given a string and a key to serve as an offset, encrypt the
    string with a Caesar Cipher and return the new ciphertext.

    Time:  O(N), where N = number of characters in the input string
    Space: O(N), where N = number of characters in the input string
    
    Last Practice: 2022-03-13 09:05:49
'''
def caesarCipherEncryptor(string, key):
	key %= 26
	ciphertext = []
	for char in string:
		ciphertext.append(encipher(char, key))
	return "".join(ciphertext)

def encipher(char, key):
	start = ord('a') - 1
	end = ord('z')
	newChar = ord(char) + key
	if newChar > end: return chr((newChar % end) + start)
	return chr(newChar)
