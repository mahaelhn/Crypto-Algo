from cryptography.hazmat.primitives import hashes, hmac

h = hmac.HMAC(key, hashes.SHA256())
h.update(b"message to hash")
h.finalize()

