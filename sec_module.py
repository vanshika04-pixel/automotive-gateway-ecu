import hashlib

def secure(data):
    return hashlib.sha256(data.encode()).hexdigest()
