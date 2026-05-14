p = 11
q = 13

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = 103

text = input("Enter Plain Text: ")

encrypted = []

# Encryption
for char in text:

    plain = ord(char)

    cipher = pow(plain, e, n)

    encrypted.append(cipher)

print("Encrypted Message:", encrypted)

decrypted = ""

# Decryption
for cipher in encrypted:

    plain = pow(cipher, d, n)

    decrypted += chr(plain)

print("Decrypted Message:", decrypted)