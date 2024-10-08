from cryptolib import aes

KEY = b'Sixteen byte key'  # 16-byte key for AES
IV = b'1234567890abcdef'   # Initialization vector for AES

def encrypt_data(plaintext):
    cipher = aes(KEY, 2, IV)
    pad_length = 16 - len(plaintext) % 16
    padded_data = plaintext + bytes([pad_length]) * pad_length
    return cipher.encrypt(padded_data)

def decrypt_data(ciphertext):
    cipher = aes(KEY, 2, IV)
    decrypted = cipher.decrypt(ciphertext)
    pad_length = decrypted[-1]
    return decrypted[:-pad_length]

def save_db(data):
    encrypted_data = encrypt_data(str(data).encode('utf-8'))
    with open('db.txt', 'wb') as f:
        f.write(encrypted_data)

def load_db():
    try:
        with open('db.txt', 'rb') as f:
            encrypted_data = f.read()
            decrypted_data = decrypt_data(encrypted_data)
            return eval(decrypted_data.decode('utf-8'))
    except OSError:
        # Initialize default database structure
        return {"users": {}}
