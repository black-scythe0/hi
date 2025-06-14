from hashlib import sha256
from secrets import token_hex





class user:

    '''
User class containig:-

'h_' in variable is for  hashes 
'b_' for """"""" "" """ bool
's_' for """"""" "" """  string.

func secure_hash_d:-

'used to generate reandom hashes'

    '''

    name :str
    b_link :bool
    key :str
    passwd :str
    
    def __init__(self, name, b_link, key, passwd):
        self.h_name = user.secure_hash_d(name)
        self.b_link = b_link  
        self.h_key = user.secure_hash_d(key)
        self.h_passwd = user.secure_hash_d(passwd)

        
    def secure_hash_d(data):
        salt = token_hex(69)
        
        return sha256((data + salt).encode()).hexdigest()




if __name__ == "__main__":
    tobject = user.secure_hash_d("hello")
    print(tobject)
