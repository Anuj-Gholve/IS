# Simplified DES Demonstration Program for Full Plaintext

# Initial Permutation Table
IP = [1, 5, 2, 0, 3, 7, 4, 6]

# Final Permutation Table
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]

# Expansion Permutation
EP = [0, 3, 1, 2, 1, 2, 3, 0]

# P4 Permutation
P4 = [1, 3, 2, 0]

# S-Boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 3, 2, 1],
    [2, 1, 0, 3]
]

S1 = [
    [0, 1, 2, 3],
    [2, 3, 1, 0],
    [1, 0, 3, 2],
    [3, 2, 0, 1]
]


# Convert Text to Binary
def text_to_binary(text):

    binary = ""

    for ch in text:
        binary += format(ord(ch), '08b')

    return binary


# Convert Binary to Text
def binary_to_text(binary):

    text = ""

    for i in range(0, len(binary), 8):

        byte = binary[i:i+8]

        text += chr(int(byte, 2))

    return text


# Permutation Function
def permute(bits, table):

    return ''.join(bits[i] for i in table)


# XOR Function
def xor(a, b):

    result = ""

    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))

    return result


# S-Box Lookup
def sbox_lookup(bits, sbox):

    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)

    value = sbox[row][col]

    return format(value, '02b')


# Feistel Function
def feistel(right, key):

    expanded = permute(right, EP)

    xored = xor(expanded, key)

    b0 = xored[:4]
    b1 = xored[4:]

    s0 = sbox_lookup(b0, S0)
    s1 = sbox_lookup(b1, S1)

    combined = s0 + s1

    output = permute(combined, P4)

    return output


# Generate Round Keys
def generate_keys(master_key):

    keys = []

    for i in range(16):

        shifted = master_key[i:] + master_key[:i]

        keys.append(shifted[:8])

    return keys


# Encryption Function for One Block
def encrypt_block(plaintext, round_keys):

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


# Decryption Function for One Block
def decrypt_block(ciphertext, round_keys):

    bits = permute(ciphertext, IP)

    left = bits[:4]
    right = bits[4:]

    for i in range(15, -1, -1):

        temp = feistel(right, round_keys[i])

        new_right = xor(left, temp)

        left = right
        right = new_right

    combined = right + left

    plain = permute(combined, IP_INV)

    return plain


# Main Program

plaintext = input("Enter Plain Text : ")
key = input("Enter Key : ")

print("Plain Text :", plaintext)
print("Key        :", key)

# Convert plaintext and key to binary
plain_binary = text_to_binary(plaintext)
key_binary = text_to_binary(key)

print("\nBinary Plain Text :")
print(plain_binary)

print("\nBinary Key :")
print(key_binary)

# Take first 10 bits from key
master_key = key_binary[:10]

# Generate round keys
round_keys = generate_keys(master_key)

print("\nRound Keys:")
for i in range(16):
    print("K", i+1, ":", round_keys[i])

# Split plaintext into 8-bit blocks
blocks = []

for i in range(0, len(plain_binary), 8):
    blocks.append(plain_binary[i:i+8])

print("\nPlaintext Blocks:")
for block in blocks:
    print(block)

# Encrypt all blocks
cipher_binary = ""

print("\nEncryption Process")

for block in blocks:
    print("\nEncrypted Character :", binary_to_text(block))
    print("Encrypting Block :", block)

    cipher_block = encrypt_block(block, round_keys)

    print("Encrypted Block :", cipher_block)

    cipher_binary += cipher_block

# Decrypt all blocks
decrypted_binary = ""

print("\nDecryption Process")

cipher_blocks = []

for i in range(0, len(cipher_binary), 8):
    cipher_blocks.append(cipher_binary[i:i+8])

for block in cipher_blocks:

    print("\nDecrypting Block :", block)

    plain_block = decrypt_block(block, round_keys)

    print("Decrypted Block :", plain_block)
    print("Decrypted Character :", binary_to_text(plain_block))

    decrypted_binary += plain_block

# Convert binary back to text
decrypted_text = binary_to_text(decrypted_binary)
encrypted_text = binary_to_text(cipher_binary)
print("\nFinal Cipher Binary :")
print(cipher_binary)
print("\nEncrypted Text :")
print(encrypted_text)
print("\nDecrypted Text :")
print(decrypted_text)
