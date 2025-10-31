import numpy as np

# --- Step 1: Convert characters to numbers ---
def text_to_numbers(text):
    text = text.upper().replace(" ", "")
    numbers = [ord(char) - 64 for char in text if char.isalpha()]  # A=1, B=2, ...
    return numbers

# --- Step 2: Convert numbers back to text ---
def numbers_to_text(numbers):
    text = ''.join([chr(int(round(num)) + 64) for num in numbers])
    return text

# --- Step 3: Pad message so its length is a multiple of matrix size ---
def pad_message(nums, size):
    while len(nums) % size != 0:
        nums.append(0)  # pad with 0 (null)
    return nums

# --- Step 4: Encode message ---
def encode_message(message, key):
    nums = text_to_numbers(message)
    nums = pad_message(nums, key.shape[0])
    nums = np.array(nums).reshape(-1, key.shape[0]).T
    encoded = np.dot(key, nums)
    return encoded

# --- Step 5: Decode message ---
def decode_message(encoded, key):
    inv_key = np.linalg.inv(key)
    decoded = np.dot(inv_key, encoded)
    decoded = np.round(decoded).astype(int).T.flatten()
    decoded = [n for n in decoded if n > 0]  # remove padding zeros
    return numbers_to_text(decoded)

# --- Example ---
message = "Linear Algebra is fun"
key = np.array([[2, 3, 1],
                [1, 1, 1],
                [1, 2, 1]])

print("Original message:", message)
print("\nKey matrix:\n", key)

# Encode
encoded = encode_message(message, key)
print("\nEncoded numeric message:\n", encoded)

# Decode
decoded = decode_message(encoded, key)
print("\nDecoded message:", decoded)
