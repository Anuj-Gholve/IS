text = "Hello World"
print("Original String:", text)
print()
print("AND with 127:")
for ch in text:
    result = ord(ch) & 127
    print(f"  '{ch}' ({ord(ch)}) AND 127 = {result} -> '{chr(result)}'")
print()
print("XOR with 127:")
for ch in text:
    result = ord(ch) ^ 127
    print(f"  '{ch}' ({ord(ch)}) XOR 127 = {result} -> '{chr(result)}'")
