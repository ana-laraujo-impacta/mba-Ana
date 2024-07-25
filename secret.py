import secrets

secret_key = secrets.token_hex(32)  # Gera uma chave secreta de 64 caracteres hexadecimais
print(secret_key)