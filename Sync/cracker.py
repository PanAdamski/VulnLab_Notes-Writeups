import hashlib

def crack_hash(hash_to_crack, secure, username, wordlist_path):
    with open(wordlist_path, "r", encoding="latin-1") as wordlist:
        for password in wordlist:
            if hashlib.md5(f"{secure}|{username}|{password.strip()}".encode()).hexdigest() == hash_to_crack:
                return password.strip()
    return None

secure = "6c4972f3717a5e881e282ad3105de01e"
wordlist_path = "/usr/share/wordlists/rockyou.txt"

hash1 = "7658a2741c9df3a97c819584db6e6b3c"
username1 = "admin"

hash2 = "a0de4d7f81676c3ea9eabcadfd2536f6"
username2 = "triss"

print(f"Hash {hash1}: {crack_hash(hash1, secure, username1, wordlist_path)}")
print(f"Hash {hash2}: {crack_hash(hash2, secure, username2, wordlist_path)}")
                                                                               
