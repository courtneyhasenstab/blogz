import hashlib

def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_pw_hash(password, hash):
    if make_pw_hash(password) == hash:
        return True
<<<<<<< HEAD
    return False
=======
    return False
>>>>>>> 78636ddf9b70dcc512e0ac52b21cc416a479bf11
