def atbash_cipher(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    result = ""

    for char in text:
        lower_char = char.lower()
        
        if lower_char in alphabet:
            index = alphabet.index(lower_char)
            new_char = reversed_alphabet[index]
            
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char

    return result


original_text = "Hello, World! 123"
encrypted = atbash_cipher(original_text)
decrypted = atbash_cipher(encrypted)

print("Original: ", original_text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

