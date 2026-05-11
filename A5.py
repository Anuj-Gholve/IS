def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
n = p * q
phi = (p - 1) * (q - 1)
for i in range(2, phi):
    if gcd(i, phi) == 1:
        e = i
        break
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break
msg = int(input("Enter message: "))
cipher = (msg ** e) % n
decrypt = (cipher ** d) % n
print("Public Key =", (e, n))
print("Private Key =", (d, n))
print("Encrypted Message =", cipher)
print("Decrypted Message =", decrypt)
