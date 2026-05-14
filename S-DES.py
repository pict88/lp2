# Simplified DES (S-DES) demo in Python
# Hardcoded key and plaintext for clarity

# Initial permutation (IP) and its inverse
IP = [1, 5, 2, 0, 3, 7, 4, 6]
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]

# Expansion/permutation (EP)
EP = [3, 0, 1, 2, 1, 2, 3, 0]

# P4 permutation
P4 = [1, 3, 2, 0]

# S-boxes
S0 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]

S1 = [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,0],
      [2,1,0,3]]

def permute(bits, table):
    return [bits[i] for i in table]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox_lookup(bits, sbox):
    row = (bits[0]<<1) | bits[3]
    col = (bits[1]<<1) | bits[2]
    val = sbox[row][col]
    return [ (val>>1)&1 , val&1 ]

def fk(bits, subkey):
    left, right = bits[:4], bits[4:]
    ep = permute(right, EP)
    temp = xor(ep, subkey)
    left_part, right_part = temp[:4], temp[4:]
    s0_out = sbox_lookup(left_part, S0)
    s1_out = sbox_lookup(right_part, S1)
    p4_out = permute(s0_out + s1_out, P4)
    return xor(left, p4_out) + right

def switch(bits):
    return bits[4:] + bits[:4]

def encrypt(plaintext, K1, K2):
    bits = permute(plaintext, IP)
    bits = fk(bits, K1)
    bits = switch(bits)
    bits = fk(bits, K2)
    return permute(bits, IP_INV)

def decrypt(ciphertext, K1, K2):
    bits = permute(ciphertext, IP)
    bits = fk(bits, K2)
    bits = switch(bits)
    bits = fk(bits, K1)
    return permute(bits, IP_INV)

# --- Demo run ---
# Hardcoded plaintext (8 bits) and subkeys
plaintext = [1,0,1,0,0,1,1,0]   # example 8-bit block
K1 = [0,1,1,0,1,0,1,1]          # subkey 1
K2 = [1,0,0,1,0,1,1,0]          # subkey 2

cipher = encrypt(plaintext, K1, K2)
print("Ciphertext:", cipher)

decrypted = decrypt(cipher, K1, K2)
print("Decrypted:", decrypted)
