A1 — Bitwise Operations (AND, OR, XOR)
What is this Practical?

Demonstrates bitwise AND, OR, and XOR operations on ASCII values of "Hello World" using value 127.

Code Explanation
ord(ch) converts character to ASCII integer.
& 127 → keeps lower 7 bits.
| 127 → sets lower 7 bits to 1.
^ 127 → flips lower 7 bits.

Example:

'H' = 72 = 01001000
72 ^ 127 = 55
Important Theory
ASCII maps characters to integers.
127 = 01111111

XOR is reversible:

A⊕K⊕K=A
AND is not reversible because information is lost.
Viva Questions & Answers
Q: What does ord() do?

A: Converts character into ASCII/Unicode integer value.

Q: Why is 127 used?

A: 127 = 01111111 in binary. It affects only lower 7 bits.

Q: Why is XOR important in cryptography?

A: XOR is reversible, fast, and widely used in encryption algorithms.

Q: Is XOR reversible?

A: Yes. A ^ K ^ K = A.

Q: What is One-Time Pad?

A: OTP uses XOR with a truly random key of same length.

Q: Difference between AND and XOR?

A: AND loses information; XOR preserves information and is reversible.

A2 — Columnar Transposition Cipher
What is this Practical?

Implements a classical transposition cipher where characters are rearranged using a key.

Code Explanation
Encryption

Find rows using:

rows = ceil(len(msg)/len(key))
Pad message using _
Fill matrix row-wise
Sort key columns
Read columns in sorted order
Decryption
Create empty matrix
Fill columns in key order
Read row-wise
Remove padding
Important Theory
Characters are rearranged, not replaced.
This is a transposition cipher.
Security is weak alone.
Viva Questions & Answers
Q: Is this substitution or transposition?

A: Transposition.

Q: Why use padding?

A: To fill the matrix completely.

Q: What does sorted(range(cols), key=lambda k:key[k]) do?

A: Sorts column indices based on alphabetical order of key letters.

Q: What if key has repeated letters?

A: Python stable sorting preserves order.

Q: Time complexity?

A: O(n)

Q: Difference between Rail Fence and Columnar Cipher?

A: Rail Fence uses zigzag pattern; Columnar uses matrix columns.

A3 — DES (Simplified Feistel Cipher)
What is this Practical?

Implements a simplified DES-like Feistel cipher using permutations, XOR, and S-Boxes.

Code Explanation
Function	Purpose
permute()	Rearranges bits
xor()	XOR operation
sbox_lookup()	S-Box substitution
feistel()	Expansion → XOR → S-Boxes → P4
generate_keys()	Generates round keys
encrypt()	Feistel encryption
decrypt()	Same process with reversed keys
Important Theory

Feistel structure:

L
i+1
	​

=R
i
	​

R
i+1
	​

=L
i
	​

⊕F(R
i
	​

,K
i
	​

)
S-Boxes provide confusion.
Permutations provide diffusion.
Decryption uses reversed keys.
Viva Questions & Answers
Q: What is a Feistel cipher?

A: Cipher structure using split halves and XOR operations.

Q: Why are S-Boxes important?

A: They provide non-linearity and confusion.

Q: How does decryption work?

A: Same algorithm with keys reversed.

Q: What is the Avalanche Effect?

A: One-bit change changes ~50% output bits.

Q: Difference between real DES and this code?

A: Real DES uses:

64-bit block
56-bit key
16 rounds
8 S-Boxes

This code is simplified for learning.

Q: Why is DES insecure?

A: 56-bit key can be brute-forced.

Q: What is Triple DES?

A: Encrypt-Decrypt-Encrypt using multiple DES keys.

A4 — AES-128
What is this Practical?

Implements AES-128 encryption and decryption in Python.

Code Explanation
Function	Purpose
sub_bytes()	S-Box substitution
shift_rows()	Row shifting
mix_columns()	Diffusion using GF(2^8)
add_round_key()	XOR with round key
key_expansion()	Generate round keys
xtime()	Multiply by 2 in GF(2^8)
gmul()	Galois multiplication
aes_encrypt()	Encryption
aes_decrypt()	Decryption
Important Theory
AES is SPN (Substitution-Permutation Network).
Block size = 128 bits.
AES-128 uses 10 rounds.
Uses GF(2^8) arithmetic.
Viva Questions & Answers
Q: Difference between AES and DES?

A: AES uses SPN; DES uses Feistel.

Q: Steps in AES round?
SubBytes
ShiftRows
MixColumns
AddRoundKey
Q: Why no MixColumns in final round?

A: AES standard removes it in final round.

Q: What is GF(2^8)?

A: Galois Field with 256 values.

Q: What is xtime()?

A: Multiply by 2 in GF(2^8).

Q: What is RCON?

A: Round constants used in key expansion.

Q: AES variants?
AES-128 → 10 rounds
AES-192 → 12 rounds
AES-256 → 14 rounds
Q: Real-world use of AES?

A: HTTPS, WiFi, VPNs, WhatsApp encryption.

A5 — RSA Algorithm
What is this Practical?

Implements RSA public-key encryption.

Code Explanation
Input primes p, q

Compute:

n = p*q
phi = (p-1)*(q-1)

Find e:

gcd(e, phi) == 1

Find d:

(e*d) % phi == 1

Encrypt:

cipher = (msg ** e) % n

Decrypt:

decrypt = (cipher ** d) % n
Important Theory
RSA is asymmetric cryptography.
Public key = (e,n)
Private key = (d,n)
Security depends on factorization difficulty.
Viva Questions & Answers
Q: Why is RSA asymmetric?

A: Uses separate public and private keys.

Q: Why must p and q be prime?

A: RSA mathematics depends on primes.

Q: Why must gcd(e, phi)=1?

A: So modular inverse d exists.

Q: What is modular inverse?

A: Number d such that:

(e×d)modϕ=1
Q: What is Euler's Totient Function?
ϕ(n)=(p−1)(q−1)
Q: Why use pow(m,e,n) in real RSA?

A: Efficient modular exponentiation.

Q: Can RSA encrypt large files?

A: No. RSA encrypts symmetric keys; AES encrypts actual data.

Q: Typical RSA key sizes?

A: 2048 or 4096 bits.

Q: What is digital signature?

A: Encrypting hash using private key.

A6 — Diffie-Hellman Key Exchange
What is this Practical?

Implements Diffie-Hellman key exchange to create a shared secret over insecure channel.

Code Explanation
Input:
Prime P
Generator G
Private keys a, b

Compute:

A = G^a mod P
B = G^b mod P

Shared secret:

s = B^a mod P
s = A^b mod P
Important Theory
DH performs key exchange, not encryption.
Security depends on Discrete Logarithm Problem.
Viva Questions & Answers
Q: Why do both users get same secret?
G
ab
=G
ba
Q: What is the Discrete Log Problem?

A: Finding exponent from:

A=G
a
modP

is computationally difficult.

Q: What is MITM attack?

A: Attacker replaces exchanged public keys.

Q: What is modular exponentiation?

A: Efficient calculation of large powers under modulo.

Q: Difference between RSA and DH?
RSA → encryption + signatures
DH → key exchange
General Theory Questions
Q: Symmetric vs Asymmetric Encryption?
Symmetric → same key (AES, DES)
Asymmetric → public/private keys (RSA)
Q: Block Cipher vs Stream Cipher?
Block → fixed-size blocks
Stream → one bit/byte at a time
Q: What are Confusion and Diffusion?
Confusion → hides key relationship
Diffusion → spreads plaintext influence
Q: What is Hybrid Encryption?

A: RSA exchanges AES key; AES encrypts data.

Q: What is the CIA Triad?
Confidentiality
Integrity
Availability
Quick Reference Table
Practical	Topic	Type
A1	Bitwise AND/OR/XOR	Basic Operations
A2	Columnar Transposition	Symmetric
A3	DES (Simplified)	Symmetric
A4	AES-128	Symmetric
A5	RSA	Asymmetric
A6	Diffie-Hellman	Key Exchange
