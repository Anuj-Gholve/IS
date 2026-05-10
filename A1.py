text = "Hello World"

print("ASCII:")
for ch in text:
    print(ord(ch), end=" ")

print("\n")

print("AND with 127:")
for ch in text:
    print(ord(ch) & 127, end=" ")

print("\n")

print("OR with 127:")
for ch in text:
    print(ord(ch) | 127, end=" ")

print("\n")

print("XOR with 127:")
for ch in text:
    print(ord(ch) ^ 127, end=" ")
    
