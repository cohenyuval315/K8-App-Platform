from cryptography.fernet import Fernet


async def generate_fernet_key() -> bytes:
    return Fernet.generate_key()


async def encrypt_string(
    secret_key: str, string: str, encoding="utf-8"
) -> str:
    cipher_suite = Fernet(secret_key)
    string_bytes = string.encode(encoding)
    encrypted_id = cipher_suite.encrypt(string_bytes)
    return encrypted_id.decode(encoding)


async def decrypt_string(
    secret_key: str, encrypted_string: str, encoding="utf-8"
) -> str:
    cipher_suite = Fernet(secret_key)
    encrypted_bytes = encrypted_string.encode(encoding)
    decrypted_string = cipher_suite.decrypt(encrypted_bytes)
    return decrypted_string.decode(encoding)
