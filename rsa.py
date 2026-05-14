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


'''
import math

# Extended Euclidean Algorithm to find modular inverse
def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception("No modular inverse exists")
    return x % phi

# RSA setup
p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)

e = 7
print("gcd(e, φ):", math.gcd(e, phi))  # must be 1

d = mod_inverse(e, phi)
print("Computed d:", d)

# Encryption
text = input("Enter Plain Text: ")
encrypted = [pow(ord(ch), e, n) for ch in text]
print("Encrypted Message:", encrypted)

# Decryption
decrypted = "".join(chr(pow(c, d, n)) for c in encrypted)
print("Decrypted Message:", decrypted)
'''
