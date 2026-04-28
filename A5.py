# RSA Algorithm - Pure Python (No Libraries)

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        return None
    return x % phi

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # find e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)
    return (e, n), (d, n)  # public key, private key

def encrypt(plain_text, public_key):
    e, n = public_key
    return [pow(ord(ch), e, n) for ch in plain_text]

def decrypt(cipher_text, private_key):
    d, n = private_key
    return ''.join(chr(pow(c, d, n)) for c in cipher_text)

# --- Main ---
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

if not is_prime(p) or not is_prime(q):
    print("Both numbers must be prime!")
else:
    public_key, private_key = generate_keys(p, q)
    print(f"\nPublic Key  (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    msg = input("\nEnter message: ")

    encrypted = encrypt(msg, public_key)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("Decrypted:", decrypted)
