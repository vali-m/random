from hashlib import sha512


class Cracker:

    def __init__(self, salt, hashed, charset, maxlen):
        self.salt = salt
        self.hashed = hashed.lower()
        self.charset = charset
        self.maxlen = maxlen
    

    def isPassword(self, pw_str):
        salted_pw = bytes(pw_str + self.salt,"utf-8")
        new_hashed = sha512(salted_pw).hexdigest()
        return self.hashed == new_hashed
    
    def backtrack(self, crt_pw = "", crt_len=0):
        if self.isPassword(crt_pw):
            print(f"Password is '{crt_pw}'!!")
            return True
        if crt_len < self.maxlen:
            for letter in self.charset:
                new_pw = crt_pw + letter
                ret = self.backtrack(new_pw, crt_len + 1)
                if ret:
                    return True
#         print(f"Tried '{crt_pw}'...")
        return False
    