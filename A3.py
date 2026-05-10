IP = [1, 5, 2, 0, 3, 7, 4, 6]
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]
EP = [3, 0, 1, 2, 1, 2, 3, 0]
P4 = [1, 3, 2, 0]
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]
S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permute(bits, table):
    return ''.join(bits[i] for i in table)

def xor(a, b):
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    value = sbox[row][col]
    return format(value, '02b')

def feistel(right, key):
    expanded = permute(right, EP)
    xored = xor(expanded, key)
    left = xored[:4]
    right_half = xored[4:]
    s0 = sbox_lookup(left, S0)
    s1 = sbox_lookup(right_half, S1)
    combined = s0 + s1
    return permute(combined, P4)

def generate_keys(master_key):
    keys = []
    for i in range(16):
        shifted = master_key[i:] + master_key[:i]
        keys.append(shifted[:8])
    return keys

def encrypt(plaintext, round_keys):
    bits = permute(plaintext, IP)
    left = bits[:4]
    right = bits[4:]
    for i in range(16):
        temp = feistel(right, round_keys[i])
        new_right = xor(left, temp)
        left = right
        right = new_right
    combined = right + left
    cipher = permute(combined, IP_INV)
    return cipher

def decrypt(ciphertext, round_keys):
    bits = permute(ciphertext, IP_INV)
    left = bits[:4]
    right = bits[4:]
    for i in range(15, -1, -1):

        temp = feistel(right, round_keys[i])
        new_right = xor(left, temp)
        left = right
        right = new_right
    combined = right + left
    plain = permute(combined, IP)
    return plain

plaintext = "10101010"

master_key = "1010000011"
round_keys = generate_keys(master_key)

print("Round Keys:")
for i in range(16):
    print("K", i+1, ":", round_keys[i])

cipher = encrypt(plaintext, round_keys)
print("\nEncrypted Text :", cipher)

decrypted = decrypt(cipher, round_keys)
print("Decrypted Text :", decrypted)
