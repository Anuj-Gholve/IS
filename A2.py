import math

def encrypt(msg, key):
    cipher = ""
    cols = len(key)
    rows = math.ceil(len(msg) / cols)
    msg += '_' * (rows * cols - len(msg))
    matrix = []
    for i in range(rows):
        matrix.append(list(msg[i * cols:(i + 1) * cols]))
    key_order = sorted(range(cols), key=lambda k: key[k])
    for col in key_order:
        for row in range(rows):
            cipher += matrix[row][col]
    return cipher

def decrypt(cipher, key):
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)
    key_order = sorted(range(cols), key=lambda k: key[k])
    matrix = [[''] * cols for _ in range(rows)]
    idx = 0
    for col in key_order:
        for row in range(rows):
            matrix[row][col] = cipher[idx]
            idx += 1
    plain = ""
    for row in range(rows):
        for col in range(cols):
            plain += matrix[row][col]
    return plain.rstrip('_')

msg = input("Enter message: ")
key = input("Enter key: ")

encrypted = encrypt(msg, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
