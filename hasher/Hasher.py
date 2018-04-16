import hashlib


def HashMD5(content):
        hashMD5 = hashlib.md5()
        hashMD5.update(content)
        return hashMD5.hexdigest()


def HashSHA512(content):
        hashSHA512 = hashlib.sha512()
        hashSHA512.update(content)
        return hashSHA512.hexdigest()

