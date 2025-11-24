import zlib
import base64

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
perm     = "5s17GF9NTMPUubWniayJSt4rjVQewZmxKkd_gc2vCXpYIh08foOH-RDE3q6ALzBl"

inv_map = {b: a for a, b in zip(alphabet, perm)}

# Ask the user for the encoded input
encoded = input("Enter the coded value: ").strip()

try:
    # Reverse the string
    step1 = encoded[::-1]

    # Undo character substitution
    step2 = "".join(inv_map.get(ch, ch) for ch in step1)

    # Base64 decode
    compressed = base64.urlsafe_b64decode(step2.encode())

    # Decompress
    original = zlib.decompress(compressed).decode()

    print("\n✅ Decoded text:")
    print(original)

except Exception as e:
    print("\n❌ Failed to decode. Possible reasons:")
    print("- Invalid encoded value")
    print("- Wrong format")
    print("- Corrupted data")
