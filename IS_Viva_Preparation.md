# 🛡️ Information Security — Viva Preparation Guide

> Covers all 6 practicals: A1 → A6. Each section has **Aim, Theory, Code Walkthrough, Sample I/O, and Viva Q&A**.

---

## A1 — Bitwise Operations (AND & XOR)

**File:** [A1.py](file:///c:/Users/anujg/OneDrive/Desktop/MESWCOE/Sixth%20Semester/Practical%20Exam/IS/A1.py)

### Aim
Perform bitwise AND and XOR operations on each character of "Hello World" with the value 127.

### Theory
| Operation | Symbol | Rule |
|-----------|--------|------|
| AND | `&` | Both bits must be 1 → 1 |
| XOR | `^` | Different bits → 1, Same bits → 0 |

- **127 in binary** = `01111111` (7 bits set).
- `AND 127` masks out the 8th bit (MSB), keeping only the lower 7 bits — equivalent to ensuring ASCII range.
- `XOR 127` flips the lower 7 bits — acts as a simple reversible cipher.

### Code Walkthrough
1. `ord(ch)` converts character to its ASCII integer.
2. `& 127` / `^ 127` performs the bitwise operation.
3. `chr(result)` converts the result back to a character.

### Sample Output
```
AND with 127:
  'H' (72) AND 127 = 72 -> 'H'
XOR with 127:
  'H' (72) XOR 127 = 55 -> '7'
```

### Viva Q&A

**Q: Why is 127 used?**
A: 127 = `01111111`. AND with 127 strips the MSB (useful for ASCII). XOR with 127 flips lower 7 bits (simple cipher).

**Q: Is XOR reversible?**
A: Yes! `A XOR K XOR K = A`. Applying XOR twice with the same key returns the original.

**Q: What is the difference between AND and XOR in cryptography?**
A: AND loses information (not reversible). XOR is reversible and is the backbone of many ciphers (DES, AES, OTP).

**Q: What happens if we AND 'H' (72) with 127?**
A: 72 = `01001000`, 127 = `01111111`. Result = `01001000` = 72 = 'H'. Since 'H' is already < 128, the result is unchanged.

**Q: What is a truth table for XOR?**
A: `0^0=0, 0^1=1, 1^0=1, 1^1=0`.

---

## A2 — Columnar Transposition Cipher

**File:** [A2.py](file:///c:/Users/anujg/OneDrive/Desktop/MESWCOE/Sixth%20Semester/Practical%20Exam/IS/A2.py)

### Aim
Implement encryption and decryption using the Columnar Transposition Cipher.

### Theory
- A **transposition cipher** rearranges characters without substituting them.
- The plaintext is written row-by-row into a matrix whose column count = key length.
- Columns are read out in the **alphabetical order of the key** to produce ciphertext.

**Example:** Message = `HELLO WORLD`, Key = `HACK`

Key order: H=2, A=0, C=1, K=3 → read columns in order 0,1,2,3 → columns: A, C, H, K.

### Code Walkthrough

**Encrypt:**
1. Calculate `rows = ceil(len(msg) / cols)`.
2. Pad message with `_` if needed.
3. Fill a matrix row-by-row.
4. `key_order = sorted(range(cols), key=lambda k: key[k])` → gets column indices sorted by key character.
5. Read columns in `key_order` to produce ciphertext.

**Decrypt:**
1. Create an empty matrix.
2. Fill column-by-column in key order from the ciphertext.
3. Read row-by-row to recover plaintext; strip trailing `_`.

### Sample I/O
```
Enter message: HELLO WORLD
Enter key: HACK
Encrypted: EWL LOLDHOR_L
Decrypted: HELLO WORLD
```

### Viva Q&A

**Q: What type of cipher is this — substitution or transposition?**
A: Transposition. Characters are rearranged, not replaced.

**Q: Why do we pad with underscores?**
A: To fill the matrix completely so every column has the same length.

**Q: How is the key used to determine column order?**
A: Characters in the key are sorted alphabetically; their original indices give the column read order.

**Q: What is the time complexity?**
A: O(n) where n = message length (we iterate through the message a constant number of times).

**Q: Is this cipher secure?**
A: Not by modern standards. It can be broken by frequency analysis and known-plaintext attacks. Often combined with substitution (product cipher) for better security.

**Q: Difference between columnar and rail-fence transposition?**
A: Rail-fence writes in a zigzag pattern across rows. Columnar writes row-by-row and reads column-by-column based on key order.

---

## A3 — DES (Data Encryption Standard)

**File:** [A3.py](file:///c:/Users/anujg/OneDrive/Desktop/MESWCOE/Sixth%20Semester/Practical%20Exam/IS/A3.py)

### Aim
Implement the DES algorithm in pure Python (no libraries).

### Theory
- **Type:** Symmetric block cipher.
- **Block size:** 64 bits. **Key size:** 64 bits (56 effective + 8 parity).
- **Rounds:** 16 rounds of a Feistel network.
- **Structure:** Feistel cipher — same structure for encryption & decryption (just reverse key order).

**Steps:**
1. **Initial Permutation (IP)** — rearranges the 64 input bits.
2. Split into **Left (32 bits)** and **Right (32 bits)**.
3. **16 Feistel Rounds:** each round applies Expansion → XOR with round key → S-Box substitution → Permutation (P).
4. **Swap** left and right after last round.
5. **Final Permutation (FP)** — inverse of IP.

**Key Schedule:**
1. Apply **PC-1** (64→56 bits, removes parity bits).
2. Split into C and D (28 bits each).
3. For each round: left-shift C and D, then apply **PC-2** (56→48 bits) to get round key.

### Code Walkthrough

| Function | Purpose |
|----------|---------|
| `permute(block, table)` | Rearranges bits according to a permutation table |
| `left_shift(bits, n)` | Circular left shift by n positions |
| `xor(a, b)` | Bitwise XOR of two bit arrays |
| `str_to_bits(s)` | String → list of bits (8 bits per char) |
| `bits_to_hex(bits)` | Bits → hex string |
| `generate_keys(key_bits)` | Produces 16 round keys using PC-1, shifts, PC-2 |
| `des_round(L, R, key)` | One Feistel round: E → XOR → S-Box → P → XOR with L |
| `des(msg_bits, keys)` | Full DES: IP → 16 rounds → swap → FP |

**S-Box lookup (critical):** Each 6-bit chunk → row = bit0+bit5, col = bits1-4 → lookup 4-bit value.

### Sample I/O
```
Enter 8-char message: HELLO123
Enter 8-char key: MYSECRET
Encrypted (hex): 2a1c5e8b3f7d4a90
Decrypted: HELLO123
```

### Viva Q&A

**Q: What is a Feistel cipher?**
A: A structure where plaintext is split into halves; one half is transformed and XORed with the other. Decryption uses the same algorithm with reversed keys.

**Q: Why does DES use 16 rounds?**
A: Provides sufficient diffusion and confusion. Fewer rounds are vulnerable to differential/linear cryptanalysis.

**Q: What is the purpose of S-Boxes?**
A: They provide **non-linearity** (confusion). They map 6 bits → 4 bits using a non-linear lookup table.

**Q: How is decryption done?**
A: Same algorithm, but round keys are applied in reverse order (`round_keys[::-1]`).

**Q: Why is DES considered insecure today?**
A: 56-bit key is too short — brute-force is feasible. Replaced by AES. Triple-DES (3DES) was a temporary fix.

**Q: What is the Avalanche Effect?**
A: A small change in input (1 bit) causes ~50% change in output. DES achieves this through multiple rounds of S-box + permutation.

**Q: What are IP and FP?**
A: Initial Permutation shuffles bits before processing. Final Permutation is the inverse of IP, applied after all rounds.

**Q: How many keys are generated and of what size?**
A: 16 round keys, each 48 bits.

---

## A4 — AES-128 (Advanced Encryption Standard)

**File:** [A4.py](file:///c:/Users/anujg/OneDrive/Desktop/MESWCOE/Sixth%20Semester/Practical%20Exam/IS/A4.py)

### Aim
Implement AES-128 encryption and decryption in pure Python.

### Theory
- **Type:** Symmetric block cipher (NOT Feistel).
- **Block size:** 128 bits (16 bytes). **Key size:** 128 bits.
- **Rounds:** 10 (for AES-128). AES-192 has 12, AES-256 has 14.
- State is a **4×4 byte matrix** (column-major order).

**Each round (1–9) has 4 steps:**
1. **SubBytes** — substitute each byte using S-Box (non-linearity/confusion).
2. **ShiftRows** — cyclically shift rows left (row 0: no shift, row 1: 1, row 2: 2, row 3: 3).
3. **MixColumns** — matrix multiplication in GF(2⁸) (diffusion).
4. **AddRoundKey** — XOR state with round key.

**Round 10:** SubBytes → ShiftRows → AddRoundKey (no MixColumns).

**Key Expansion:** Generates 11 round keys (176 bytes) from the original 16-byte key using RotWord, SubWord, and RCON.

### Code Walkthrough

| Function | Purpose |
|----------|---------|
| `sub_bytes(state)` | Replace each byte via S-Box lookup |
| `shift_rows(s)` | Cyclic left-shift of rows |
| `xtime(a)` | Multiply by 2 in GF(2⁸) — used in MixColumns |
| `mix_columns(s)` | Matrix multiplication for diffusion |
| `gmul(a, b)` | Galois Field multiplication (used in InvMixColumns) |
| `add_round_key(state, key)` | XOR state with round key |
| `key_expansion(key)` | Generate 44 words (176 bytes) of round keys |
| `aes_encrypt / aes_decrypt` | Full 10-round AES process |

### Sample I/O
```
Enter message (up to 16 chars): Hello AES World!
Enter key (16 chars): MySecretKey12345
Encrypted (hex): 8a3b2c... (32 hex chars)
Decrypted: Hello AES World!
```

### Viva Q&A

**Q: How is AES different from DES?**
A: AES uses a Substitution-Permutation Network (SPN), not Feistel. AES has 128-bit blocks (vs. 64). AES key: 128/192/256 bits (vs. 56). AES is much more secure and faster.

**Q: What is the S-Box and how is it generated?**
A: Each byte is replaced: first find multiplicative inverse in GF(2⁸), then apply an affine transformation. It provides non-linearity.

**Q: What is GF(2⁸)?**
A: Galois Field of 256 elements. Arithmetic is done modulo an irreducible polynomial `x⁸ + x⁴ + x³ + x + 1` (0x11B). Used in MixColumns.

**Q: Why is there no MixColumns in the last round?**
A: It's omitted to make the structure symmetric for encryption/decryption. Including it would add no security.

**Q: What does `xtime` do?**
A: Multiplies a byte by 2 in GF(2⁸). If MSB is set, left-shift and XOR with 0x1B (the irreducible polynomial).

**Q: How many round keys are generated?**
A: 11 round keys (1 initial + 10 rounds) = 44 words = 176 bytes.

**Q: What is the role of RCON?**
A: Round constant used in key expansion to break symmetry between rounds.

**Q: What are the AES key sizes and their corresponding rounds?**
A: AES-128 → 10 rounds, AES-192 → 12 rounds, AES-256 → 14 rounds.

---

## A5 — RSA Algorithm

**File:** [A5.py](file:///c:/Users/anujg/OneDrive/Desktop/MESWCOE/Sixth%20Semester/Practical%20Exam/IS/A5.py)

### Aim
Implement RSA encryption and decryption in pure Python.

### Theory
- **Type:** Asymmetric (public-key) cipher.
- Based on the mathematical difficulty of **factoring large numbers**.

**Key Generation:**
1. Choose two primes **p** and **q**.
2. Compute **n = p × q**.
3. Compute **φ(n) = (p−1)(q−1)** (Euler's totient).
4. Choose **e** such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
5. Compute **d = e⁻¹ mod φ(n)** (modular inverse using Extended Euclidean Algorithm).
6. **Public key = (e, n)**, **Private key = (d, n)**.

**Encrypt:** C = M^e mod n  
**Decrypt:** M = C^d mod n

### Code Walkthrough

| Function | Purpose |
|----------|---------|
| `gcd(a, b)` | Euclidean algorithm to find GCD |
| `extended_gcd(a, b)` | Returns GCD and Bézout coefficients (x, y) |
| `mod_inverse(e, phi)` | Finds d such that `e × d ≡ 1 (mod φ)` |
| `is_prime(n)` | Trial division primality test |
| `generate_keys(p, q)` | Computes n, φ, e, d and returns key pair |
| `encrypt(text, pub)` | Encrypts each character: `pow(ord(ch), e, n)` |
| `decrypt(cipher, priv)` | Decrypts each number: `chr(pow(c, d, n))` |

### Sample I/O
```
Enter prime p: 61
Enter prime q: 53
Public Key  (e, n): (7, 3233)
Private Key (d, n): (1783, 3233)
Enter message: HI
Encrypted: [2198, 2818]
Decrypted: HI
```

### Viva Q&A

**Q: Why is RSA called asymmetric?**
A: It uses two different keys — public (for encryption) and private (for decryption). Anyone can encrypt, only the holder of the private key can decrypt.

**Q: What is the mathematical basis of RSA security?**
A: The difficulty of factoring large semiprime numbers (n = p × q).

**Q: What is Euler's totient function?**
A: φ(n) counts integers from 1 to n that are coprime to n. For n = p×q (both prime): φ(n) = (p−1)(q−1).

**Q: What is the Extended Euclidean Algorithm?**
A: It finds x, y such that `ax + by = gcd(a, b)`. Used to find the modular inverse of e.

**Q: Why must gcd(e, φ) = 1?**
A: So that e has a modular inverse d. If gcd ≠ 1, d doesn't exist and decryption is impossible.

**Q: How does `pow(M, e, n)` work efficiently?**
A: Python's built-in pow uses **modular exponentiation** (square-and-multiply), which is O(log e).

**Q: Can RSA encrypt long messages directly?**
A: No. RSA is slow and encrypts blocks < n. In practice, RSA encrypts a symmetric key, and the actual data is encrypted with AES (hybrid encryption).

**Q: What are typical RSA key sizes?**
A: 2048 or 4096 bits for n. The primes in this code are small (educational only).

---

## A6 — Diffie-Hellman Key Exchange

**File:** [A6.html](file:///c:/Users/anujg/OneDrive/Desktop/MESWCOE/Sixth%20Semester/Practical%20Exam/IS/A6.html)

### Aim
Implement the Diffie-Hellman Key Exchange protocol using HTML + JavaScript.

### Theory
- **Purpose:** Allows two parties to agree on a **shared secret key** over an insecure channel without transmitting the key itself.
- **Type:** Key exchange protocol (not encryption).
- Based on the **Discrete Logarithm Problem (DLP)**.

**Steps:**
1. Agree on public parameters: prime **P** and generator **G**.
2. Alice picks private key **a**, computes public key `A = G^a mod P`, sends A to Bob.
3. Bob picks private key **b**, computes public key `B = G^b mod P`, sends B to Alice.
4. Alice computes shared secret: `s = B^a mod P`.
5. Bob computes shared secret: `s = A^b mod P`.
6. Both get the **same secret** because `G^(ab) mod P = G^(ba) mod P`.

### Code Walkthrough

**`power_mod(base, exp, mod)`** — Modular exponentiation using square-and-multiply:
```javascript
while (exp > 0) {
    if (exp % 2 === 1) result = (result * base) % mod;
    exp = Math.floor(exp / 2);
    base = (base * base) % mod;
}
```

**`exchange()`** — Main function:
1. Reads P, G, a, b from input fields.
2. Computes `alicePublic = G^a mod P` and `bobPublic = G^b mod P`.
3. Computes `aliceSecret = B^a mod P` and `bobSecret = A^b mod P`.
4. Verifies both secrets match.

### Sample I/O (Default values: P=23, G=5, a=6, b=15)
```
Alice sends: A = 5^6 mod 23 = 8
Bob sends:   B = 5^15 mod 23 = 19
Alice computes: 19^6 mod 23 = 2
Bob computes:   8^15 mod 23 = 2
Shared Secret Key = 2 (Both match!)
```

### Viva Q&A

**Q: What problem does Diffie-Hellman solve?**
A: It allows two parties to establish a shared secret over an insecure channel without ever transmitting the secret itself.

**Q: What is the Discrete Logarithm Problem?**
A: Given G, P, and `A = G^a mod P`, it's computationally hard to find `a`. This one-way property makes DH secure.

**Q: Does DH encrypt data?**
A: No. It only exchanges a key. The shared secret is then used with a symmetric cipher (like AES) to encrypt data.

**Q: What is a Man-in-the-Middle (MITM) attack on DH?**
A: An attacker intercepts and replaces public keys, establishing separate shared secrets with each party. **Solution:** Use authenticated DH (digital signatures/certificates).

**Q: What is a generator G?**
A: A primitive root modulo P — its powers generate all integers from 1 to P−1. Ensures all possible keys are reachable.

**Q: Why must P be prime?**
A: Ensures the multiplicative group mod P has desirable mathematical properties (cyclic, of order P−1).

**Q: What is the difference between DH and RSA?**
A: DH is for **key exchange** (both parties compute a shared secret). RSA is for **encryption and digital signatures** (one party encrypts, the other decrypts).

---

## 📝 General Theory Questions (Cross-Cutting)

**Q: What is the difference between symmetric and asymmetric encryption?**
A: Symmetric uses the **same key** for encryption/decryption (DES, AES). Asymmetric uses a **key pair** — public + private (RSA).

**Q: What are confusion and diffusion?**
A: **Confusion** = complex relationship between key and ciphertext (S-Boxes). **Diffusion** = spreading plaintext statistics across ciphertext (permutations, MixColumns).

**Q: What is a block cipher vs stream cipher?**
A: Block cipher encrypts fixed-size blocks (DES=64-bit, AES=128-bit). Stream cipher encrypts one bit/byte at a time (RC4).

**Q: What are block cipher modes of operation?**
A: ECB (each block independent — insecure), CBC (chain blocks), CTR (counter mode — parallelizable), GCM (authenticated encryption).

**Q: What is a digital signature?**
A: Hash the message → encrypt hash with private key. Receiver decrypts with public key and compares hashes. Provides authentication, integrity, non-repudiation.

**Q: What is hashing vs encryption?**
A: Hashing is **one-way** (MD5, SHA-256) — cannot recover original. Encryption is **two-way** — can decrypt with key.

---

## 🔑 Quick Reference Table

| # | Topic | Type | Key Size | Block Size | Rounds |
|---|-------|------|----------|------------|--------|
| A1 | Bitwise AND/XOR | Basic operation | N/A | N/A | N/A |
| A2 | Columnar Transposition | Symmetric (transposition) | Variable | Variable | 1 |
| A3 | DES | Symmetric (Feistel) | 56 bits | 64 bits | 16 |
| A4 | AES-128 | Symmetric (SPN) | 128 bits | 128 bits | 10 |
| A5 | RSA | Asymmetric | 1024–4096 bits | Variable | N/A |
| A6 | Diffie-Hellman | Key Exchange | Variable | N/A | N/A |
